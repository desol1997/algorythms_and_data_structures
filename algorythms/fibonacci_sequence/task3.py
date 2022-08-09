# Given integers 1 <= n <= 10^18 and 2 <= m <= 10^5.
# You need to find the remainder after dividing the n-th Fibonacci number by m.

# Sample Input:
# 10 2

# Sample Output:
# 1

# The solution uses an idea of Pisano period https://en.wikipedia.org/wiki/Pisano_period.


def fib_mod(n, m):
    assert n >= 1
    assert m >= 2

    if n == 1:
        return 1
    else:
        a, b = 0, 1
        remainder_series = [0, 1]

        while True:
            a, b = b, a + b
            remainder_series.append(b % m)
            if remainder_series[-2] == 0 and remainder_series[-1] == 1:
                remainder_series = remainder_series[:-2]
                period = len(remainder_series)
                return remainder_series[n % period]


print(fib_mod(5, 3))
