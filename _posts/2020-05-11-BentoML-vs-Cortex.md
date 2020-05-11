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
        <td>Can be packaged, saved via Python command to <a href="https://docs.bentoml.org/en/latest/concepts.html#customizing-model-repository">management repository with a web dashboard</a> or PyPI</td>
        <td>Packaging only via Docker images without explicit support</td>
    </tr>
    <tr>
        <td>Horizontal scaling</td>
        <td>Configured separately in other clustering tools. Working on an opinionated Kubernetes deployment.</td>
        <td>Is part of Cortex configs. But is thus less flexible (private cloud, HTTPS deploy requires custom scripts)</td>
    </tr>
    <tr>
        <td>User interface</td>
        <td>CLI, Web UI</td>
        <td>CLI</td>
    </tr>
    <tr>
        <td>Metrics</td>
        <td>Prometheus metrics</td>
        <td>AWS EKS metrics</td>
    </tr>
    <tr>
        <td>API Auto-Docs</td>
        <td>Swagger/OpenAPI</td>
        <td>n/a?</td>
    </tr>
    <tr>
        <td>User support</td>
        <td>responsive <a href="https://join.slack.com/t/bentoml/shared_invite/enQtNjcyMTY3MjE4NTgzLTU3ZDc1MWM5MzQxMWQxMzJiNTc1MTJmMzYzMTYwMjQ0OGEwNDFmZDkzYWQxNzgxYWNhNjAxZjk4MzI4OGY1Yjg">unpaid Slack Channel</a>, but Slack is not the best tool for support</td>
        <td>very responsive <a href="https://gitter.im/cortexlabs/cortex">Gitter</a></td>
    </tr>
    <tr>
        <td>Suggest anything else?</td>
        <td></td>
        <td></td>
    </tr>
</tbody>
</table>

