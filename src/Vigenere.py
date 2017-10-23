alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_alphabet = []


def set_alphabet(password):
    while password.__len__() < alphabet.__len__():
        password += password
    for i in range(0, alphabet.__len__()):
        new_alphabet.append(password[i])


def encode(words, password="password"):
    set_alphabet(password)
    output = ''
    for char in words:
        if alphabet.__contains__(char.lower()):
            output += new_alphabet[alphabet.index(char.lower())]
    return output


# TODO fix this somehow
def decode(words, password="password"):
    set_alphabet(password)
    output = ''
    for char in words:
        if alphabet.__contains__(char.lower()):
            output += alphabet[new_alphabet.index(char.lower())]
    return output

if __name__ == '__main__':
    while True:
        user_input = input()
        print(encode(user_input))
