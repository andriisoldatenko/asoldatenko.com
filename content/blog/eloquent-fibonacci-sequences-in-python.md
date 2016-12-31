Title: Eloquent fibonacci sequences in python
Date: 2016-12-31 21:30
Category: Python
Tags: python,tips,tricks,python3,fibonacci
Slug: eloquent-fibonacci-sequences-in-python
Authors: Andrii Soldatenko


## Quick introduction
The idea of this article to collect eloquent python patterns using well-known
Fibonacci sequence.

## Recursive approach
```
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)
```

## Recursive approach using caching
```
import functools


@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)
```

## 
```
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
    a, b = b, a + b
```