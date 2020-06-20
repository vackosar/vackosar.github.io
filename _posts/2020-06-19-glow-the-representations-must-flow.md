---
layout: post
title: "Glow - The Representations Must Flow"
date: 2020-06-19
categories: ML
description: Get interpretable latent representations by composing non-linear invertible functions and maximizing the exact log-likelihood.
image: https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/glow-drawing.png
permalink: /:categories/:title
---

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

Flow-based models are the odd machines in the corner of the neural network laboratory capable of calculating the exact log-likelihood of any provided sample.
Discover their arcane qualities on a representative example of [Glow from OpenAI](https://d4mucfpksywv.cloudfront.net/research-covers/glow/paper/glow.pdf) and its ability to [unlock secrets of human visual illusions](https://arxiv.org/pdf/2005.08772v1.pdf).


<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/glow-drawing.png"
        alt="Glow flow-based model architecture diagram" />
    <figcaption class="figure-caption">Glow flow-based model architecture diagram</figcaption>
</figure>


## Flow-Based Model vs VAE and GAN
Advantages of flow-based models are:
1. Exact latent-variable inference and log-likelihood (invertible) compared to approximate VAE (compressed) and absent GAN representations (discriminated).
1. Easy to parallelize both synthesis and inference.
1. Useful latent space similar to VAE, but richer as it is not compressed.
1. With respect to depth constant memory requirements for gradient calculations thanks to invertibility.


## The Likelihood Goal


The goal is to find an invertible function \\( F \\), which under assumption of multi-variate normal distribution with isotropic unit variance
on the latent space gives maximum likelihood. The change of variables of probability density function formula means that above is equivalent to minimizing below.
\\( -\sum_x( \log(P_X(x))) = - \sum_x  \log(p_Z (f(x))) + \log | \det(\frac{\partial F(x)}{\partial x} ) | \\)

where \\( f \\) maps from the data space \\(  X \\) to the latent space \\( Z \\). The requirement of normal distribution on the latent space gives us:

\\(  p_Z(f(x)) = \frac{1}{\sqrt{2\pi}} \exp( - \frac{f(x)^ 2}{2} ) \\).

We choose the function to be made by composition of multiple simpler functions.

\\(  F = f \circ f \circ f ... \circ f \\)

We can look at these as special layers of neural networks since the non-linearity used is convolutional layer.

## Invertible building block

The invertible function is constructed as composition of K trainable non-linear invertible functions.

\\( I_1 \cup I_2 = \\{1, 2, 3, ..., d\\} \\)
and
\\( I_1 \cap I_2 = \\{\\} \\)
and usually
\\( |I_1| = |I_2| = d / 2 \\).

Then transformation called _affine coupling_ below can be inverted. Additionally inverse calculation costs as much as forward.

\\( y_{I_1} = x_{I_1} \\)

\\( y_{I_2} = x_{I_2} s(x_{I_1}) + t(x_{I_1}) \\)


Determinant of Jacobian of above transformation is non zero and cheap to calculate by design.

\\( \det [\partial y / \partial x] = \exp[ \sum_{j \in I_2} s_j(x_{I_1}) ] \\)

With above can apply non-linearity to just half of the dimensions. We perform additional learnable invertible linear operation \\( W \\) to remix them before non-linearity is applied in each layer.
Since \\( W \\) maps only in the channel dimension and not spacial, it can be interpreted as \\( 1 \times 1 \\) convolution.
This is the origin of the Glow paper subtitle.


## The Neural Network Non-linearities

The non-linear functions \\( s \\) and \\( t \\) in above are convolutional neural networks. They are constructed to have sufficient number of features, such that number of input and output channels are equal.
But how do we go from an image to required number of channels for above to make sense? We create 4 new channels by splitting the image into four parallel images via skip-one-pixel sub-sampling.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/glow-masking.png"
        alt="Skip-one-pixel - squeezing operation from Real NVP paper"/>
    <figcaption class="figure-caption">Skip-one-pixel - squeezing operation image from Real NVP paper</figcaption>
</figure>


## Human Visual Illusions

Two dimensional images are poor stand-ins for three dimensional world. Infinite 3D scenes collapse into identical picture after projection to 2D, making the reversion problem ill-posed.
A paper has [a statistical story of visual illusions](https://arxiv.org/pdf/2005.08772v1.pdf) to tell thanks to Glow flow-based model. 
Illusions seem to raise thanks to visual system perceiving unlikely images as even less probable. For example increasing saturation contrast between patches of images.
The brain here seems to err on side of contrast here.
You shouldn't believe me that two images below contain same image patches in the middle.
Download the image, cut up the middle sections, and move them closer together to verify that they indeed are of same color.

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/glow-illusion.png"
        alt='Visual illusion from paper "A Statistical Story of Visual Illusions".'/>
    <figcaption class="figure-caption">Cut up the middle sections, and move them closer together to verify that they indeed are of same color. <a href="https://arxiv.org/pdf/2005.08772v1.pdf)">source</a></figcaption>
</figure>


## Quiz TODO

Retain what you have just read by taking training quiz generated from this article.<br>
<br>
<!-- <a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=d0dfd88a-4712-42a6-bec3-68c86133d1ce">StarSpace Quiz</a> -->


## Source Papers

- [Glow: Generative Flow with Invertible 1×1 Convolutions](https://d4mucfpksywv.cloudfront.net/research-covers/glow/paper/glow.pdf); 2018; Diederik P. Kingma, Prafulla Dhariwal; OpenAI, San Francisco.
- [Density Estimation Using Real NVP](https://arxiv.org/pdf/1605.08803.pdf); 2016; Laurent Dinh, Jascha Sohl-Dickstein, Samy Bengio
- [NICE: Non-linear Independent Components Estimation](https://arxiv.org/pdf/1410.8516.pdf); 2014; Laurent Dinh, David Krueger, Yoshua Bengio
- [A Statistical Story of Visual Illusions](https://arxiv.org/pdf/2005.08772v1.pdf); 2020; Elad Hirsch, Ayellet Tal