# Given an integer 1 <= n <= 40. You need to calculate the n-th Fibonacci number (recall that F0 = 0, F1 = 1 and
# Fn = Fn-1 + Fn-2 for n >= 2).

from functools import lru_cache


@lru_cache(maxsize=None)
def fib1(n):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    assert n >= 0

    if n == 0:
        return 0
    else:
        a, b = 0, 1

        for _ in range(n - 1):
            a, b = b, a + b
        return b


print(fib1(8))
print(fib2(40))
