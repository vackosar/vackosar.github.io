---
layout: post
title: "Python with statement exception handling"
date: 2020-04-08
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
```bash
db connection acquired this is param value
this is the connection
rolling back due to ex hello
returning db connection to a pool
```

