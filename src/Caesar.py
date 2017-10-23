import string


def encode(words, number=13):
    output = ''

    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[number:] + alphabet[:number]

    for letter in words.lower():
        if letter in alphabet:
            output += shifted_alphabet[alphabet.index(letter)]

    return output


def decode(words, number=-13):
    return encode(words, number)

if __name__ == '__main__':
    while True:
        user_input = input()
        print(encode(user_input))
