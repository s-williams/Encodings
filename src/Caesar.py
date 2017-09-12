import string


def encode(words, number=5):
    output = ''

    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[number:] + alphabet[:number]

    for letter in words.lower():
        output += shifted_alphabet[alphabet.index(letter)]

    return output

if __name__ == '__main__':
    user_input = input()

    print(encode(user_input))