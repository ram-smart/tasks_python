def get_binary_from_integer(number: int):
    """возвращает двоичное число целого десятичного в виде строки"""
    if number == 0:
        return '0'

    binary_number = ''
    while number != 0:
        bit = number % 2
        binary_number = str(bit) + binary_number
        number = (number - bit) // 2

    return binary_number


def get_integer_from_binary(number: str):
    """возвращает десятичное число двоичного"""
    int_number = 0
    revers_number = number[::-1]

    for i in range(0, len(revers_number)):
        bit = int(revers_number[i])
        int_number = int_number + (bit * pow(2, i))

    return int_number


def get_binary_sum(number1: str, number2: str):
    """возвращает сумму двоиных чисел в виде строки двочиного числа"""
    int_number1 = get_integer_from_binary(number1)
    int_number2 = get_integer_from_binary(number2)

    sum_int = int_number1 + int_number2
    result = get_binary_from_integer(sum_int)

    return result


def get_binary_sum_2(number_1, number_2):
    """возвращает сумму двоиных чисел в виде строки двочиного числа"""
    binary_1 = int(number_1, base=2)
    binary_2 = int(number_2, base=2)
    return bin(binary_1 + binary_2).replace('0b', '')
