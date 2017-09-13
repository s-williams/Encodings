import string


def get_binary_value(letter):
    if letter.lower() in string.ascii_lowercase:
        return format(ord(letter.lower()), 'b')[2:]
    return ''


def encode(word):
    output = ''
    for letter in word:
        output += get_binary_value(letter)
    return output

if __name__ == '__main__':
    while True:
        user_input = input()

        print(encode(user_input))
