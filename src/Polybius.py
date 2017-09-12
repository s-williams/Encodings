polybius = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'k'],
            ['l', 'm', 'n', 'o', 'p'],
            ['q', 'r', 's', 't', 'u'],
            ['v', 'w', 'x', 'y', 'z']]


def get_poly_value(letter):
    for k in range(5):
        for j in range(5):
            if letter == polybius[k][j]:
                return str(k + 1) + str(j + 1)
    return ''


def encode(word):
    output = ''

    for letter in word:
        output += get_poly_value(letter)

    return output

if __name__ == '__main__':
    user_input = input()

    print(encode(user_input))
