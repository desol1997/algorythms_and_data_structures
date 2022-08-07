# Given number 1 <= n <= 10^9
# find the maximum number k for which n can be represented as the sum of k distinct natural terms.
# Print the number k in the first line, and k terms in the second line.


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
