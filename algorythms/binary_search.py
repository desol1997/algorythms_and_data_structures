# The first line contains an integer 1 <= n <= 10^5 and an array A[1...n] of n distinct natural numbers
# not exceeding 10^9 in ascending order, the second - an integer 1 <= k <= 10^5 and k natural numbers b1,...,bk
# not exceeding 10^9. For each i from 1 to k you need to print the index 1 <= j <= n for which A[j] = bi or -1
# if there is no such j.

# Sample Input:
# 5 1 5 8 12 13
# 5 8 1 23 1 11

# Sample Output:
# 3 1 -1 1 -1

import sys


def binary_search(k, n_numbers, array_length):
    left, right = 0, array_length - 1
    while left <= right:
        m = left + (right - left) // 2
        if n_numbers[m] == k:
            return m + 1
        elif n_numbers[m] > k:
            right = m - 1
        else:
            left = m + 1
    return -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *n_numbers = next(reader)
    _, *k_numbers = next(reader)

    result = []
    for k in k_numbers:
        index = binary_search(k, n_numbers, n)
        result.append(index)

    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
