---
layout: post
title: To What Python Number Types Does json.loads Parse?
date: 2020-08-25
last_modified_at: 2022-06-06
categories: software
description: JSON specifies only a number value, so how to infer the correct type between int and float? How are NaN and Infinity handled?
image: /images/json.loads-and-numbers.png
permalink: /:categories/:title
my_related_post_paths:
- _posts/2024-01-24-How-To-Install-Your-Python-Version-On-Ubuntu.md
- _posts/2022-06-04-transformer-embeddings-and-tokenization.md
- _posts/2017-06-04-Code-Structure-Principles.md
- _posts/2023-12-29-Danger-of-Python-Lambda-Late-Binding.md
- _posts/2023-03-24-Symbolic-vs-Connectionist-Machine-Learning.md
- _posts/2022-08-03-Strong-Static-Typing-vs-Weak-Dynamic-Typing.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
---



{% include highlight-rouge-friendly.css.html %}

## How JSON handles numbers?
[JSON ECMA](https://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf) leaves mapping of the human-readable format to correct language type to the programming language:
<blockquote style="font-style: italic" class="blockquote">
JSON is agnostic about the semantics of numbers. In any programming language, there can be a variety of number types of various capacities and complements, fixed or floating, binary or decimal. That can make interchange between different programming languages difficult. JSON instead offers only the representation of numbers that humans use: a sequence of digits. All programming languages know how to make sense of digit sequences even if they disagree on internal representations. That is enough to allow interchange.
</blockquote>


## How json.loads selects number types?

Here is a code snippet with its standard output below it:
```python
import json
for v in json.loads("[2000, 20.0, 20.1, 1e6, NaN, Infinity, -Infinity]"):
    print(f"{v}: {type(v)}")
```

```text 
2000: <class 'int'>
20.0: <class 'float'>
20.1: <class 'float'>
1000000.0: <class 'float'>
nan: <class 'float'>
inf: <class 'float'>
-inf: <class 'float'>
```

[Python documentation](https://docs.python.org/3.4/library/json.html#encoders-and-decoders) also explains that `NaN, Infinity, -Infinity` are not actually part of JSON standard, but that they are interpreted anyway:
<blockquote style="font-style: italic" class="blockquote">
It also understands NaN, Infinity, and -Infinity as their corresponding float values, which is outside the JSON spec.
</blockquote>

The conversion is similar to conversion from a Python source code. The number becomes `int` only in case of non-scientific format without a dot. Otherwise you'll get a `float`.

Read also on this blog how to [wrap you resource creation and closure into context manager with-statement and catch exceptions there](/software/Python-Context-Manager-With-Statement-Exception-Handling).