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
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1
```
