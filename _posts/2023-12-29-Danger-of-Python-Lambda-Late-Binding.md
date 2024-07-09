---
title: 'Dangers of Python Lambda: Repeated Values due to Late Binding'
description: Avoid hidden bugs due to unexpected values in loops with AsyncIO or Multi-threading Python.
layout: post
categories: software
date: 2023-12-29
last_modified_at: 2023-12-29
permalink: /:categories/:title
image: /images/python-lambda-late-binding-repeated-final-value-bug-error.png
my_related_post_paths:
- _posts/2024-06-09-Bash-Tricks-I-Use.md
- _posts/2020-08-25-to-what-python-number-types-does-json.loads-parse.md
- _posts/2024-01-24-How-To-Install-Your-Python-Version-On-Ubuntu.md
- _posts/2020-04-08-Python-Context-Manager-With-Statement-Exception-Handling.md
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2019-08-28-1D-Kalman-Is-Exponential-Or-Cumulative-Average.md
- _posts/2022-08-03-Strong-Static-Typing-vs-Weak-Dynamic-Typing.md
---

{% include highlight-rouge-friendly.css.html %}

There may be a scary secret problem in your use of lambda in Python, when used with [AsyncIO or Multi-threading](https://medium.com/@glami-engineering/the-bridge-between-sync-and-async-world-23cb25e57182). It is called Late Binding.

## The Question
Can you see what is unexpected about below results of the [DocTest](https://docs.python.org/3/library/doctest.html)?
By the way, you are familiar with `add_done_callback` method, right?

```
async def process(i):
    await asyncio.sleep(2)
    print(i, end=', ')


async def process_all():
    """
    >>> asyncio.run(process_all())
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19,
    """

    tasks = []
    for i in range(10):
        task = asyncio.create_task(process(i))
        # will this lambda change value?
        task.add_done_callback(lambda _task: asyncio.create_task(process(i + 10)))
        tasks.append(task)
        await asyncio.sleep(0.1)

    await asyncio.gather(*tasks)
    await asyncio.sleep(2)
```

## The Answer
The output values are all stuck on final value of `19`!
Always assign all variables that you are using the lambda with AsyncIO or threading.
Or create an object that will carry the specific values intended to be used during later execution of the function preventing them to change.


## Fix for unexpected final values in my Python loop with a lambda
The repeated `19` in the results is due to the late binding behavior of closures in Python. The lambda function captures the variable `i` by reference, not by value. By the time the lambda is executed, the for loop has completed and `i` has its final value of `9`. When `i + 10` is evaluated inside the lambda, it always equals `19`.


```
async def process(i):
    await asyncio.sleep(2)
    print(i, end=', ')


async def process_all():
    """
    >>> asyncio.run(process_all())
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    """

    tasks = []
    for i in range(10):
        task = asyncio.create_task(process(i))
        # will this lambda change value?
        # task.add_done_callback(lambda task: asyncio.create_task(process(i + 10)))
        # Instead of above, capture the current value of i by passing it to the lambda.
        task.add_done_callback(lambda _task, _i = i: asyncio.create_task(process(_i + 10)))
        tasks.append(task)
        await asyncio.sleep(0.1)

    await asyncio.gather(*tasks)
    await asyncio.sleep(2)
```


Try for yourself, switch the lines above and see the difference in results. Can you run a [DocTest](https://docs.python.org/3/library/doctest.html)? It is also a useful tip for You.

Is either [AsyncIO or multi-threading not so clear? Then read this as it could help](https://medium.com/@glami-engineering/the-bridge-between-sync-and-async-world-23cb25e57182).