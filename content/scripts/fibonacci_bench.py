import itertools


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    from timeit import timeit
    print(timeit("list(itertools.islice(fibonacci_generator(), 5))",
                 setup="from __main__ import fibonacci_generator"))
