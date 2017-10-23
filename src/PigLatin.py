vowels = ['a', 'e', 'i', 'o', 'u']


def encode(words):
    output = ''
    for word in words.split(' '):
        if word.lower()[0] in vowels:
            output += word + "-ay "
        else:
            output += word[1:] + "-" + word[0] + "ay "
    return output


def decode(words):
    output = ''
    for word in words.split(' '):
        if word[:-2][-1] != '-':
            output += word[:-2][-1] + word[:-4] + " "
        else:
            output += word[:-3] + " "
    return output

if __name__ == '__main__':
    while True:
        user_input = input()
        print(encode(user_input))
