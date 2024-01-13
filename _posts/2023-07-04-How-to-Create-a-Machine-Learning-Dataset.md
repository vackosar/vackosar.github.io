---
title: How to Create a Machine Learning Dataset
description: Trade-offs and time investment in publishing a dataset for reproducible research and advertising.
categories: ml
date: 2023-07-04
last_modified_at: 2023-07-04
image: /images/glami-1m-multilingual-image-text-dataset-text-vs-image-similarity.png
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-03-20-massivetext-dataset-pretraining-deepminds-gopher.md
- _posts/2020-05-11-BentoML-vs-Cortex.dev--ML-Serving-Showdown.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2022-09-01-Multimodal-Image-Text-Classification.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
- _posts/2023-08-19-Validate-Reliability-of-Research-Paper.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
---

{% include image.html src="/images/glami-1m-multilingual-image-text-dataset-text-vs-image-similarity.png" alt="GLAMI-1M" %}

Dataset papers can serve as an advertising, authority, and reputation building for the releasing company.
Datasets are critical for reproducible research.
In heavily participated in creating [multilingual image-text classification dataset GLAMI-1M](https://github.com/glami/glami-1m) and writing the corresponding paper.
Here are my learning points:


### Trade-offs
The main trade offs in building of the dataset:

- Directed at specific academic research vs application real industry problem? Your academia is interested in the super long-term and often very hypothetical.

- Optimized for adoption (very small, simple to understand, translated to English, familiar models, source code available) vs optimized for research (large to download, niche academic language)

- Large dataset vs perfectly clean dataset?


### Time investment

Works on GLAMI-1M started around July 2022 and finished in January 2023 making it around 6 months of part-time effort of mostly 1 person (me), but around 30% of the time 2-4 people. I can imagine though, that this can be significantly shortened.
Considering the points below may help you to speed this up.

The dataset itself was relatively easy to create. But lots of time was spent on:

- Cleaning the dataset. Especially you need to make sure that you can understand, measure, minimize the overlap between training and the test set. Where your labels come from and are they good?

- Statistics about the dataset. Answer the most common questions that people will have. For example diversity, duplication, and richness of the samples.

- Training baseline models for the dataset and demonstrations, publishable code and Jupyter notebooks. In GLAMI-1M for example, I used [OpenAI's CLIP](/ml/OpenAIs-Image-Text-Model-CLIP) to show correlations between the [image and text features and for classification](/ml/Multimodal-Image-Text-Classification).

- Researching existing research. What is special about your dataset and why are people interested? You may have something special, but you need to read what is already out there and what is missing and highlight that.

- Writing the paper. This helps to crystallize further what is important and what you want to say, and what you suggest people do with the dataset. Additionally, you may want to publish elsewhere than just a journal or conference.



### Other Important Points

- Personally identifiable information: In the text dataset with customer responses, it will be very important to also strip all PII (personally identifiable information). I don't have experience with this, but I may be able to find out some methods if you get stuck on this.

- Source data license: Find out if you need approval of the source data owners.

- Dataset License: Some companies restrict the dataset access and require agreements acceptance, e.g., preventing Commercial use. We opted for maximum distribution ease instead with Apache 2.0 license.

- Dataset naming as Advertising: You have opportunity to increase your visibility by naming the dataset, while leaving options for other dataset you may want to release?

- Dataset storage: You may want to upload somewhere to take care of DDOS and hosting costs. While we uploaded to Zenodo for free, I then discovered that downloading speed was a big issue for us with our large dataset and also uploaded to HuggingFace.



Good luck!