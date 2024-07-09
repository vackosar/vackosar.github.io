---
layout: post
title: Python Context Manager Exception Handling and Retrying
date: 2020-04-08
last_modified_at: 2022-06-06
categories: software
description: Wrap your resource into a context manager with-statement to catch, handle exceptions, and close the resource.
permalink: /:categories/:title
image: /images/python-context-manager-close-resource-on-exception.png
redirect_from:
- /2020/04/08/Python-with-statement-exception-handling.html
- /software/Python-with-statement-exception-handling
my_related_post_paths:
- _posts/2024-01-24-How-To-Install-Your-Python-Version-On-Ubuntu.md
- _posts/2024-06-09-Bash-Tricks-I-Use.md
- _posts/2017-12-03-Boundary-Control-Entity-Architecture--The-Pattern-to-Structure-Your-Classes.md
- _posts/2017-06-04-Code-Structure-Principles.md
- _posts/2020-07-05-Transfigure-Stress-Into-Energy.md
- _posts/2023-12-29-Danger-of-Python-Lambda-Late-Binding.md
- _posts/2020-05-11-BentoML-vs-Cortex.dev--ML-Serving-Showdown.md
---



{% include highlight-rouge-friendly.css.html %}
  
{% include image.html src="/images/python-context-manager-close-resource-on-exception.png" alt="python close resource with context manager on exception" %}

One case use context manager to handle exceptions during execution of the with statement as can be seen in the snippet below. This is useful for example for rolling back database transactions in case of an exception, where the database connections can be retrieved from and returned to a connection pool.

```python
from contextlib import contextmanager


@contextmanager
def managed_resource(param):
    try:
        print(f"db connection acquired {param}")
        yield "this is the connection"

    except Exception as e:
        print(f"rolling back due to ex {e}")
        raise

    finally:
        print("returning db connection to a pool")


with managed_resource("this is param value") as connection:
    print(connection)
    raise ValueError("hello")
```

Execution of above prints below.
```
db connection acquired this is param value
this is the connection
rolling back due to ex hello
returning db connection to a pool
Traceback (most recent call last):
  File ".../test/test.py", line 36, in <module>
    raise ValueError("hello")
ValueError: hello
```

## Without The With

What happens when we try to use `managed_resource` without `with`?

Nothing. Returned object is only holds a reference to a generator and has `__enter__()` and `__exit__()` methods. The context object will only return a value from the generator upon `__enter__()` call, and will run the rest of the code after `yield` during `__exit__()` call.


## Alternative Error Handling In Exit Method
Instead of the `contextmanager` wrapper you can implement `__enter__` and `__exit__` methods on our custom object like below:

```python
class ManagedResource:

    def __init__(self, param):
        self.param = param

    def __enter__(self):
        print(f"db connection acquired {self.param}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"rolling back due to ex {exc_val}")

        print("returning db connection to a pool")


with ManagedResource("this is param value") as connection:
    print(connection)
    raise ValueError("hello")
```

Execution of above prints below.

```

db connection acquired this is param value
<__main__.ManagedResource object at 0x7f0dc9b1af70>
rolling back due to ex hello
returning db connection to a pool
Traceback (most recent call last):
  File "/home/vackosar/src/vackosar.github.io/test/test.py", line 42, in <module>
    raise ValueError("hello")
ValueError: hello
```



## Retries Using Context Manager Are Not Possible - Here Is An Alternative

Do you need to retry when for example storage is momentarily not available?
However, You cannot implement retries of the code wrapped in `with`.
You simply cannot execute `yield` multiple times.
Instead, you can pass a callback to retry method containing a exponential backoff for loop below. 

```python
def retry_on_exception(
    fun: Callable,
    args=(),
    kwargs: Optional[dict] = None,
    retry_exceptions: Tuple = (Exception,),
    max_retries: int = 3,
    base_sleep_secs: float = 3.0,
):
    if kwargs is None:
        kwargs = dict()

    ex = None
    for retry in range(max_retries + 1):
        try:
            val = fun(*args, **kwargs)
            return val

        except retry_exceptions as e:
            ex = e
            sleep_secs = base_sleep_secs * 2 ** retry
            sleep(sleep_secs)

    raise RuntimeError(f"Too many retries ({max_retries}) of {fun.__name__}") from ex
```


## Other Useful Posts
BCE architecture is [the simplest way to structure your source code files](/software/Boundary-Control-Entity-Architecture-The-Pattern-to-Structure-Your-Classes), read all about it in [my post on BCE](/software/Boundary-Control-Entity-Architecture-The-Pattern-to-Structure-Your-Classes).

Did you know that you can implement [functional ForEach in Bash](/software/Functional-Foreach-In-Bash)?
