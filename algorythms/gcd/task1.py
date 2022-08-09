# Given two numbers 1 <= a, b <= 2 * 10^9.
# Find their greatest common division.

# Sample Input 1:
# 18 35

# Sample Output 1:
# 1

# Sample Input 2:
# 14159572 63967072

# Sample Output 2:
# 4

import random


def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0


def gcd1(a, b):
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d


def gcd2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def gcd3(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)


def gcd4(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)


print(gcd1(8, 3))
print(test(gcd1))

print(gcd2(1000000, 10000))
print(test(gcd2))

print(gcd3(16, 12))
print(test(gcd3))

print(gcd3(10000, 500))
print(test(gcd4))
