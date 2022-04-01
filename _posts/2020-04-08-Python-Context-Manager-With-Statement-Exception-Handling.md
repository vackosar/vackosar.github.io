---
layout: post
title: "Handle Exception and Close Resource Using Python Context Manager With-Statement"
date: 2020-04-08
categories: software
description: Wrap you resource creation and closure into context manager with-statement and catch exceptions there.
permalink: /:categories/:title
redirect_from:
  - /2020/04/08/Python-with-statement-exception-handling.html
  - /software/Python-with-statement-exception-handling
---

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
```

# Without The With

What happens when we try to use `managed_resource` without `with`?

Nothing. Returned object is only holds a reference to a generator and has `__enter__()` and `__exit__()` methods. The context object will only return a value from the generator upon `__enter__()` call, and will run the rest of the code after `yield` during `__exit__()` call.


# Retries Using Context Manager Are Not Possible - Here Is An Alternative

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


# Other Useful Posts
BCE architecture is [the simplest way to structure your source code files](/software/Boundary-Control-Entity-Architecture-The-Pattern-to-Structure-Your-Classes), read all about it in [my post on BCE](/software/Boundary-Control-Entity-Architecture-The-Pattern-to-Structure-Your-Classes).

Did you know that you can implement [ForEach in Bash](/software/Functional-Foreach-In-Bash)?
