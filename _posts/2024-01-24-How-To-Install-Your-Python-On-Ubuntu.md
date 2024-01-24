---
title: 'How to Install Your Python Version on Ubuntu'
description: No need for Deadsnakes nor Apt, use pyenv or conda instead! 
layout: post
categories: software
date: 2024-01-24
last_modified_at: 2023-12-29
permalink: /:categories/:title
image: /images/ubuntu-install-python-pyenv-conda-thumb.png
---

![How to Install Your Python Version on Ubuntu](/images/ubuntu-install-python-pyenv-conda-thumb.png)


{% include highlight-rouge-friendly.css.html %}

You want to install a specific Python version, e.g., Python 3.9, on Ubuntu 23.10; neither Ubuntu PPA nor Deadsnakes PPA distributes it.
Fortune has it; you don't have to compile CPython from the source manually.
And you don't have to change your Ubuntu to an LTS version, e.g., 23.04 or 24.04, where Deadsnakes PPA supports your version.

You have these options:
- pyenv
- conda


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


## I hope this helps
This is a webpage I wanted to find, when a college was having this problem.
I hope it helps you now.