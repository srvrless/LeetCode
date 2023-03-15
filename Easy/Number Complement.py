num = 5


def findComplement():
    table = str.maketrans('10', '01')
    new_string = bin(num)[2:].translate(table)
    return int(new_string, 2)


print(findComplement())