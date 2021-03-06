---
layout: post
title: "BentoML vs Cortex - ML Serving Showdown"
categories: ML
date: 2020-05-11
image: /images/bentoml-cortex-logos.webp
description: To find the best model serving tool, compare open-source MLOps platforms BentoML and Cortex.
permalink: /:categories/:title
video: aU95dBAspr0
redirect_from:
  - /ml/2020/05/11/BentoML-vs-Cortex.html
  - /ml/BentoML-vs-Cortex
---


<p><img src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/bentoml-cortex-logos.webp" alt="BentoML and Cortex logo" style="width: 200px"/></p>

Updated 2021-02-21.
Do you need a simple way to train and host your machine learning AI models in the cloud?
Here is my experience with Cortex Labs's Cortex.
My view on BentoML is based on cursory overview of their documentation.
Checkout also AWS App Runner option at the end.

## Common
- both deploy and serve models via API
- both support major ML frameworks (TensorFlow, Pytorch)
- both have good documentation

## Comparison
<table border="1" class="dataframe">
<thead>
    <tr>
        <th scope="col">
            Feature
        </th>
        <th scope="col">
            <a href="https://www.bentoml.org">BentoML.org</a> 
        </th>
        <th scope="col">
            <a href="https://www.cortex.dev/">Cortex.dev</a> 
        </th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Language</td>
        <td>fully Python - easier to modify?</td>
        <td>Go & Python wrapper (Updated)</td>
    </tr>
    <tr>
        <td>Deployment</td>
        <td>Delegated to other tools: Docker, Kubernetes, AWS Lambda, SageMaker, GCP, Azule ML and more.</td>
        <td>Works currently only with local Docker and AWS EKS, GCP (Updated)</td>
    </tr>
    <tr>
        <td>Service configuration</td>
        <td>from Python</td>
        <td>from <a href="https://pypi.org/project/cortex/">Python</a> (Updated)</td>
    </tr>
    <tr>
        <td>Service packaging and distribution</td>
        <td>Can be packaged, saved via Python command to <a href="https://docs.bentoml.org/en/latest/concepts.html#customizing-model-repository">management repository with a web dashboard</a> or PyPI</td>
        <td>Packaging only via Docker images without explicit support</td>
    </tr>
    <tr>
        <td>Horizontal scaling</td>
        <td>Configured separately in other clustering tools. Working on an opinionated Kubernetes deployment.</td>
        <td>Configurable in Cortex. May be less flexible (private cloud deploy may require custom scripts)</td>
    </tr>
    <tr>
        <td>User interface</td>
        <td>CLI, Web UI</td>
        <td>CLI</td>
    </tr>
    <tr>
        <td>Metrics</td>
        <td>Prometheus metrics</td>
        <td>Prometheus metrics (Updated)</td>
    </tr>
    <tr>
        <td>API Auto-Docs</td>
        <td>Swagger/OpenAPI</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>User support</td>
        <td>Responsive <a href="https://join.slack.com/t/bentoml/shared_invite/enQtNjcyMTY3MjE4NTgzLTU3ZDc1MWM5MzQxMWQxMzJiNTc1MTJmMzYzMTYwMjQ0OGEwNDFmZDkzYWQxNzgxYWNhNjAxZjk4MzI4OGY1Yjg">unpaid Slack Channel</a>, but Slack is not the best tool for support</td>
        <td>Very responsive <a href="https://gitter.im/cortexlabs/cortex">Gitter</a> and now <a href="https://join.slack.com/t/cortex-dot-dev/shared_invite/zt-lf58axgy-0QkLZzFSSku5_Jybd9yiZQ">Slack</a></td>
    </tr>
    <tr>
        <td>Suggest anything else?</td>
        <td></td>
        <td></td>
    </tr>
</tbody>
</table>
<br>

## My Experience with Cortex

Here is [a blog post on Cortex use at GLAMI](https://medium.com/@aiteamglami/serve-your-ml-models-in-aws-using-python-9908a4127a13).
It is a bit outdated take as Cortex now has its own wrapper.
Consider using this [Cortex client for Python](https://github.com/glami/cortex-serving-client), which is a Python wrapper around Cortex CLI that we use at GLAMI for MLOps.
It has couple of extra features, that keep us using it for now.

Video:
{% include load_video.html %}

## AWS App Runner
If you need super simple deployment of CPU only applications with auto-scaling you can consider using [AWS App Runner](https://aws.amazon.com/apprunner/).
You just fill in your source code repository and you app gets hosted in the selected region on your domain with auto certificate renewal.

## External Discussions
- <a href="https://www.reddit.com/r/MachineLearning/comments/ghikdz/d_is_this_fair_bentoml_vs_cortex_comparison/">Reddit discussion</a>

