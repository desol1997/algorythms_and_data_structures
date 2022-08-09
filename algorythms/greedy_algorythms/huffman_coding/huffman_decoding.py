# Restore the string by its code and unprefixed character code.

# The first line of the input file contains two space-separated integers
# k and l — the number of different letters in the string and the size of the resulting encoded string, respectively.
# The next k lines contain letter codes in the format "letter: code". Neither code is a prefix of another.
# The letters can be listed in any order.
# Only lowercase letters of the Latin alphabet can be used as letters;
# each of these letters occurs at least once in the string.
# Finally, the last line contains the encoded string. The original string and codes of all letters are non-empty.
# The given code is such that the encoded string has the smallest possible size.

# In the first line of the output file print the line s.
# It must consist of lowercase letters of the Latin alphabet.
# It is guaranteed that the length of the correct answer does not exceed 10^4 characters.

# Sample Input 1:
# 1 1
# a: 0
# 0

# Sample Output 1:
# a

# Sample Input 2:
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111

# Sample Output 2:
# abacabad


def huffman_decoding(coded_string, letters_codes):
    coded_letter = ''
    decoded_string = ''
    for letter in coded_string:
        coded_letter += letter
        if coded_letter in letters_codes:
            decoded_string += letters_codes.get(coded_letter)
            coded_letter = ''

    return decoded_string


def main():
    k = int(input().split()[0])

    letters_codes = {}
    for _ in range(k):
        letter_code = [i.strip() for i in input().split(':')]
        letters_codes[letter_code[1]] = letter_code[0]

    coded_string = input()
    decoded_string = huffman_decoding(coded_string, letters_codes)
    print(decoded_string)


if __name__ == '__main__':
    main()
