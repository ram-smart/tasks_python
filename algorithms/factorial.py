#! Программа вычисления факториала


def factorial():
    while True:
        number = int(input("Введите число \n"))
        i = 1
        result = 1
        if number == 0:
            print("Факториал числа {0} равен {1} \n".format(number, result))
        else:
            while i <= number:
                result *= i
                i += 1
            print("Факториал числа {0} равен {1} \n".format(number, result))


# Использование цикла for
def factorial_2():
    result = 1
    number = int(input("Введите число \n"))
    for i in range(1, number + 1):
        result *= i
    print("Факториал числа {0} равен {1} \n".format(number, result))


factorial_2()