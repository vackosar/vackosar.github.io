---
layout: post
title: "BentoML vs Cortex"
categories: ML
date: 2020-05-11
description: To serve ML models, this post compares major open source platforms BentoML and Cortex.
---

Note, however, that I have much more experience with Cortex.

## Common
- deploy and serve models via API
- support major ML frameworks (TensorFlow, Pytorch)

## Comparison
<table border="1" class="dataframe">
<thead>
    <tr>
        <th scope="col">
            Feature
        </th>
        <th scope="col">
            BentoML.org
        </th>
        <th scope="col">
            Cortex.dev
        </th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Language</td>
        <td>Python - easier to modify, integrate?</td>
        <td>Go</td>
    </tr>
    <tr>
        <td>Deployment</td>
        <td>Abstracted away to Docker, Kubernetes, AWS Lambda, SageMaker, Azule ML and more.</td>
        <td>Works currently with Docker and AWS EKS</td>
    </tr>
    <tr>
        <td>Service configuration</td>
        <td>via decorators directly in Python code.</td>
        <td>via YAML files</td>
    </tr>
    <tr>
        <td>Service packaging and distribution</td>
        <td>packaged and saved via Python command to [management repository with a web dashboard](https://docs.bentoml.org/en/latest/concepts.html#customizing-model-repository)</td>
        <td>Packaging only via Docker images without explicit support</td>
    </tr>
    <tr>
        <td>Horizontal scaling</td>
        <td>configured outside?</td>
        <td>is part of Cortex configs</td>
    </tr>
    <tr>
        <td>Suggest anything else?</td>
        <td></td>
        <td></td>
    </tr>
</tbody>
</table>

