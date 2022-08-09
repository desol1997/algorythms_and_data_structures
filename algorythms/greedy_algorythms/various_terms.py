# Given number 1 <= n <= 10^9
# find the maximum number k for which n can be represented as the sum of k distinct natural terms.
# Print the number k in the first line, and k terms in the second line.

# Sample Input 1:
# 4

# Sample Output 1:
# 2
# 1 3

# Sample Input 2:
# 6

# Sample Output 2:
# 3
# 1 2 3


def various_terms(n):
    terms_list = []
    for i in range(1, n + 1):
        if n >= i:
            terms_list.append(i)
            n -= i
        else:
            terms_list[-1] += n
            break

    return terms_list


def main():
    number = int(input())
    terms = various_terms(number)
    print(len(terms))
    print(' '.join([str(term) for term in terms]))


if __name__ == '__main__':
    main()
