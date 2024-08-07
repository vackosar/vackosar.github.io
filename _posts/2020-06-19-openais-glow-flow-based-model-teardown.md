---
layout: post
title: OpenAI's Glow - Flow-Based Model Teardown
date: 2020-06-19
categories: ml
description: Interpretable latent representations by composing non-linear invertible functions and maximizing the exact log-likelihood.
image: /images/glow-drawing.png
video: oJNUZzXE7n4
permalink: /:categories/:title
last_modified_at: 2022-04-16
redirect_from:
- /ml/glow-the-representations-must-flow
my_related_post_paths:
- _posts/2022-04-13-openai-dall-e-2-and-dall-e-1.md
- _posts/2021-01-02-Feed-Forward-Self-Attendion-Key-Value-Memory.md
- _posts/2020-10-25-Performers-FAVOR+-Faster-Transformer-Attention.md
- _posts/2020-11-29-Lambda-Networks-Transform-Self-Attention.md
- _posts/2022-03-05-transformers-self-attention-mechanism-simplified.md
- _posts/2023-08-25-How-Deep-Neural-Networks-Learn.md
- _posts/2023-07-29-Feature-wise-Linear-Modulation-Layer.md
---



{% include mathjax.html %}

{% include load_video.html %}

Flow-based (normalizing flow) models are the odd machines in the corner of the neural network laboratory capable of calculating the exact log-likelihood for every sample.
Discover their arcane qualities on a representative example of [OpenAI's Glow](https://d4mucfpksywv.cloudfront.net/research-covers/glow/paper/glow.pdf) and its ability to [unveil secrets of visual illusions](https://arxiv.org/pdf/2005.08772v1.pdf).
Note that you can create [interpretable latent representations also using disentangled representation training](/ml/manipulate-item-attributes-via-disentangled-representation).


## Flow-Based Model vs VAE and GAN
Advantages of flow-based models are:
1. Exact latent-variable inference and log-likelihood (invertible) compared to approximate VAE (compressed) and absent GAN representations (discriminated). (Excluding [potential numerical problems](https://arxiv.org/abs/2006.09347)).
2. Easy to parallelize both synthesis and inference (Exceptions include [autoregressive flow models](https://lilianweng.github.io/lil-log/2018/10/13/flow-based-deep-generative-models.html#models-with-autoregressive-flows)).
3. Useful latent space similar to VAE, but richer as it is not compressed.
4. With respect to depth constant memory requirements for gradient calculations thanks to invertibility.

Flow based models have similarities to diffusion models like [DALL-E 2 or GLIDE](/ml/openai-dall-e-2-and-dall-e-1).


## Normalizing Flow Models
- flow-based models are more general than [normalizing flow](https://arxiv.org/abs/1505.05770)
- flow-based stands for invertible (bijective) transformation 
- normalizing stands for desired normal distribution on the output
- use-cases thanks to mapping to simple normal distribution:
  - anomaly or defect detection as low probability samples
  - sample generation and sample interpolation and representation manipulation


## The Glow Model Architecture
- Glow model is Normalizing flow

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        data-src="/images/glow-drawing.png"
        alt="Glow flow-based model architecture diagram" />
    <figcaption class="figure-caption">Glow flow-based model architecture diagram</figcaption>
</figure>


### The Likelihood Goal

The goal is to find an invertible function \\( F \\), which under assumption of multi-variate normal (gaussian) distribution with isotropic unit variance (Independent and Identically Distributed)
on the latent space gives maximum likelihood. The change of variables of probability density function formula means that above is equivalent to minimizing below.

\\( -\sum_x( \log(P_X(x))) \\) \\( = - \sum_x  \log(p_Z (F(x))) \\) \\( + \log \mid \det(\frac{\partial F(x)}{\partial x} ) \mid \\),

where \\( F \\) maps from the data space \\(  X \\) to the latent space \\( Z \\). The requirement of normal distribution on the latent space gives us:

\\(  p_Z(F(x)) = \frac{1}{\sqrt{2\pi}} \exp( - \frac{F(x)^ 2}{2} ) \\).

We choose the function \\( F \\) to be composed of multiple simpler learnable functions \\( f \\).

\\(  F = f \circ f \circ f ... \circ f \\)

We can look at these compositions as special layers of neural networks since the non-linearities used are convolutional neural networks.

### Invertible Building Block

The invertible function \\( F \\) composed of \\( K \\) trainable non-linear invertible functions \\( f \\).

Let \\( I_1 \cup I_2 = \\{1, 2, 3, ..., d\\} \\) and \\( I_1 \cap I_2 = \\{\\} \\) and usually \\( \mid I_1 \mid = \mid I_2 \mid = d / 2 \\).

Then transformation called _affine coupling_ below can be inverted. Additionally, inverse calculation costs as much as forward.

\\( y_{I_1} = x_{I_1} \\)

\\( y_{I_2} = x_{I_2} s(x_{I_1}) + t(x_{I_1}) \\)


Determinant of Jacobian of above transformation is non zero and cheap to calculate by design.

\\( \det [\partial y / \partial x] = \exp[ \sum_{j \in I_2} s_j(x_{I_1}) ] \\)

With above can apply non-linearity to just half of the dimensions. We perform additional learnable invertible linear operation \\( W \\) to remix them before non-linearity is applied in each layer.
Since \\( W \\) maps only in the channel dimension and not in the spacial, it can be interpreted as 1×1 convolution.
This gave the Glow paper subtitle "Generative Flow with Invertible 1×1 Convolutions".


### Neural Network Non-linearities

The non-linear functions \\( s \\) and \\( t \\) in above are convolutional neural networks. They are constructed to have sufficient number of features, such that number of input and output channels are equal.
But how do we go from an image to required number of channels for above to make sense? We create 4 new channels by splitting the image into four parallel images via skip-one-pixel sub-sampling.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        data-src="/images/glow-masking.png"
        alt="Skip-one-pixel - squeezing operation from Real NVP paper"/>
    <figcaption class="figure-caption">Skip-one-pixel - squeezing operation image from <a href="https://arxiv.org/pdf/1605.08803.pdf">Real NVP paper</a></figcaption>
</figure>

## Attribute Manipulation
On the latent space it is possible to identify directions correspoding to change of certain semantic attributes.
For example there is a direction into which face could be modified to smile more.
This is an example of [a disentangled representation](/ml/manipulate-item-attributes-via-disentangled-representation).

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        data-src="/images/disentangle-smiling.png"
        alt="Glow model smiling vector"/>
    <figcaption class="figure-caption">Glow model smiling vector (<a href="https://arxiv.org/pdf/1605.08803.pdf">source</a>)</figcaption>
</figure>

## Human Visual Illusions
Ability to calculate the exact likelihood has surprising application in the study of human experience.

A paper has [a statistical story of visual illusions](https://arxiv.org/pdf/2005.08772v1.pdf) to tell thanks to the Glow model. 
The paper focuses on a common misjudgment of color brightness of image centers in which background was darkened or lightened, as shown in the image below.
The misperceptions seem to arise due to the visual system highlighting unlikely parts of the images.
The authors study this by changing the brightness picture's center and calculating the likelihood of created samples.

For example, in the image below, most people perceive the two middle patches as having a different color.
This phenomenon is called simultaneous brightness contrast.
The brain here seems to err on the side of contrast, tricking us into seeing patch colors more differentiated from the background.
You shouldn't believe me that two images below contain the same image patches in the middle.
Download the image, cut out the middle sections, and move them next to each other to verify that they indeed are of the same color. 


<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        data-src="/images/glow-illusion.png"
        alt='Simultaneous brightness contrast visual illusion from paper "A Statistical Story of Visual Illusions".'/>
    <figcaption class="figure-caption">Cut out the middle sections and move them next to each other to verify that they indeed are of the same color. <a href="https://arxiv.org/pdf/2005.08772v1.pdf)">Img source.</a></figcaption>
</figure>

In another example in the paper, they claim that the likelihood of a patch having lower saturation than the actual value is the true measure of human color saturation perception.
They call this quantity percentile rank.
I did one more experiment, which I was missing from the paper, testing this hypothesis.
I increased saturation on one of the samples by 24%, such that the percentile rank would match on both images, and now I see the same colors! Do you?

<figure class="figure">
    <img
        class="figure-img img-fluid rounded lazyload"
        data-src="/images/glow-contrast-illusion-saturation.png"
        alt='Simultaneous brightness contrast visual illusion: After saturation increase to match percentile ranks, the colors are perceived as the same.'/>
    <figcaption class="figure-caption">After saturation increase to match percentile ranks, I see the same colors! Do you?</figcaption>
</figure>

## 1-Minute Quiz

Retain what you have just read by taking training quiz generated from this article.<br>
<br>
<a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=b9a650a9-28c5-41c6-b5d0-cceb2c0988df">Flow-based model Glow micro-training quiz</a>


## Video

[https://youtu.be/oJNUZzXE7n4](https://youtu.be/oJNUZzXE7n4)


## Discussions

Insightful comments:
- [Reddit Machine Learning discussion](https://www.reddit.com/r/MachineLearning/comments/hcprze/d_glow_the_representations_must_flow/)

## Read Next
[Manipulate Item Attributes via Disentangled Representation](/ml/manipulate-item-attributes-via-disentangled-representation)