# Given the number 1 <= n <= 10^7.
# You need to find the last digit of the n-th Fibonacci number.

# Sample Input:
# 841645

# Sample Output:
# 5


def fib_last_digit(n):
    assert n >= 1
    a, b = 0, 1
    last_digit = 1

    for _ in range(n - 1):
        last_digit = (a + b) % 10
        a, b = b, last_digit

    return last_digit
