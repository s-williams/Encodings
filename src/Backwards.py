def encode(words):
    output = ''
    for word in words.split(' '):
        letters = []
        for char in word:
            letters.append(char)
        for i in range(letters.__len__()):
            output += letters.pop()
        output += ' '
    return output


def decode(words):
    encode(words)

if __name__ == '__main__':
    while True:
        user_input = input()
        print(encode(user_input))
