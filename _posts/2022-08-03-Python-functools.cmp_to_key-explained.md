---
layout: post
title: "Python functools.cmp_to_key Explained"
date: 2022-08-03
last_modified_at: 2022-08-03
categories: software
description: Understand internals of the comparison to key function quickly.
permalink: /:categories/:title
---

{% include highlight-rouge-friendly.css.html %}


Function [functools.cmp_to_key documentation](https://docs.python.org/3/library/functools.html#functools.cmp_to_key
) is a bit mysterious.
In short, function cmp_to_key creates a class that implements comparison methods is then used by Python to compare any two values. 
Let's look at a following snippet to quickly understand more. 
  

```python
from functools import cmp_to_key


def compare(x: str, y: str) -> int:
    return int(x) - int(y)


key = cmp_to_key(compare)
print(key)
print(key("10").__lt__(key("11")))
```

Execution of above prints below.
```
<functools.KeyWrapper object at 0x7f90d3fe79d0>
true
```

If you go to [the source code](https://github.com/python/cpython/blob/f9433fff476aa13af9cb314fcc6962055faa4085/Lib/functools.py#L206) you'll find out that you are getting just a class that implements comparison in a new way.

```python
def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        __slots__ = ['obj']
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        __hash__ = None
    return K
```

You can read more [on sorting in Python docs](https://docs.python.org/3/howto/sorting.html#the-old-way-using-the-cmp-parameter).


## Other Useful Posts
- [Python Context Manager Exception Handling and Retrying](https://vaclavkosar.com/software/Python-Context-Manager-With-Statement-Exception-Handling).
- BCE architecture is [the simplest way to structure your source code files](/software/Boundary-Control-Entity-Architecture-The-Pattern-to-Structure-Your-Classes), read all about it in [my post on BCE](/software/Boundary-Control-Entity-Architecture-The-Pattern-to-Structure-Your-Classes).
- Did you know that you can implement [functional ForEach in Bash](/software/Functional-Foreach-In-Bash)?
