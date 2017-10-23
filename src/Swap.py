def encode(words):
    output = ''
    for word in words.split(' '):
        letters = []
        for char in word:
            letters.append(char)
        for i in range(0, letters.__len__() - 1, 2):
            first = letters[i]
            second = letters[i + 1]
            letters[i] = second
            letters[i + 1] = first
        output += ''.join(str(x) for x in letters) + ' '
    return output


def decode(words):
    return encode(words)

if __name__ == '__main__':
    while True:
        user_input = input()
        print(decode(user_input))
