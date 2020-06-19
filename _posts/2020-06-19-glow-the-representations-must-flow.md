---
layout: post
title: "Glow - The representations must flow"
date: 2020-06-19
categories: ML
description: Compose non-linear invertible functions, maximize exact log-likelihood and get interpretable latent representation.
image: https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/glow-drawing.png
permalink: /:categories/:title
---


<p><img src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/glow-drawing.png" alt="Glow flow model architecture diagram"/></p>

## Flow-Based Model vs VAE and GAN
1. Exact latent-variable inference and log-likelihood (invertible) compared to approximate VAE (compressed) and absent GAN representations (discriminated).
1. Easy to parallelize both synthesis and inference.
1. Useful latent space similar to VAE, but richer as it is not compressed.
1. With respect to depth constant memory requirements for gradient calculations thanks to invertibility.


## Invertible building block

The goal is to find an invertible function, which under assumption of multi-variate normal distribution with isotropic unit variance on the latent space gives maximum likelihood.
The invertible function is constructed as composition of K trainable non-linear invertible functions.

<img src="https://render.githubusercontent.com/render/math?math=I_1 \cup I_2 = {1, 2, 3, ..., d}">
and
<img src="https://render.githubusercontent.com/render/math?math=I_1 \cap I_2 = {}">
Then transformation to `y` below is can be inverted:
<img src="https://render.githubusercontent.com/render/math?math=y_{I_1} = x_{I_1}">
<img src="https://render.githubusercontent.com/render/math?math=y_{I_2} = x_{I_2} * s(x_{I_1}) + t(x_{I_1})">

While determinant of Jacobian of above transformation is:
<img src="https://render.githubusercontent.com/render/math?math=det \partial y / \partial x = exp[ s(x_{I_1}) ]">


# TODO

## Source Paper

"[Glow: Generative Flow with Invertible 1×1 Convolutions](https://d4mucfpksywv.cloudfront.net/research-covers/glow/paper/glow.pdf)" with publication date 2017-11-21.
Authors: Diederik P. Kingma, Prafulla Dhariwal
Organization: OpenAI, San Francisco



## Quiz TODO

Retain what you have just read by taking training quiz generated from this article.<br>
<br>
<!-- <a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=d0dfd88a-4712-42a6-bec3-68c86133d1ce">StarSpace Quiz</a> -->


