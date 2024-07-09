---
title: How to Install Your Python Version on Ubuntu
description: No need for Deadsnakes nor Apt, use pyenv or conda instead!
layout: post
categories: software
date: 2024-01-24
last_modified_at: 2024-03-05
permalink: /:categories/:title
image: /images/ubuntu-install-python-pyenv-conda-thumb.png
redirect_from:
- /software/How-To-Install-Your-Python-On-Ubuntu
my_related_post_paths:
- _posts/2023-01-24-fill-versions-from-python-environment.md
- _posts/2021-07-01-Quilt-data-versioning-review-how-to.md
- _posts/2024-06-09-Bash-Tricks-I-Use.md
- _posts/2017-06-04-Code-Structure-Principles.md
- _posts/2018-02-25-Creating-Custom-Ubuntu-Web-Link-App.md
- _posts/2020-05-11-BentoML-vs-Cortex.dev--ML-Serving-Showdown.md
- _posts/2020-04-08-Python-Context-Manager-With-Statement-Exception-Handling.md
---

{% include image.html src="/images/ubuntu-install-python-pyenv-conda-thumb.png" alt="How to Install Your Python Version on Ubuntu" %}

{% include highlight-rouge-friendly.css.html %}

You want to install a specific Python version, e.g., Python 3.9, on Ubuntu 23.10; neither Ubuntu PPA nor Deadsnakes PPA distributes it.
Fortune has it; you don't have to compile CPython from the source manually.
And you don't have to change your Ubuntu to an LTS version, e.g., 23.04 or 24.04, where Deadsnakes PPA supports your version.

You have these options:
- pyenv (Simple Python Version Management)
- conda (Anaconda or Miniconda)
- asdf (tool version manager)
- Docker (containerized Python possible but complex)


## Pyenv
pyenv lets you easily switch between multiple versions of Python.
Each version is compiled on your machine for you and for most popular versions the compilation should work reliably. 
- Follow [installation process here](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation).
- Then you can run `pyenv install 3.9` and it should compile it from source.


## Conda
Conda instead provides [precompiled version of Python for different platforms](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html).
Although the support may not be guaranteed and a compilation fallback is an option.
In contrast to pyenv, conda is an environment manager and a package manager, so you can create multiple separate environments and install different precompiled packages into them.
- [Install conda from here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).
- Then you can create an environment: `conda create -n my-python-3.9-environment python=3.9`
- Then you need to activate the environment: `conda activate my-python-3.9-environment`


## asdf
Appears to be [popular](https://news.ycombinator.com/item?id=30917354), but I have no experience with it.
Here is an [example](https://rednafi.com/python/install_python_with_asdf/).

```
asdf install python 3.7.4
```


## Docker
This is the least practical but the most flexible and reliable approach.
Dokcer is usually only used to run single version applications.
Docker is not intended as a development environment.
But there is a support for IDE's like [Pycharm to run a Python interpreter in Docker containers](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html).


## I hope this helps
This is a webpage I wanted to find, when a college was having this problem.
I hope it helps you now.