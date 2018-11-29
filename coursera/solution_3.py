import sys
from math import pow, sqrt
"""Программа для решения квадратного уравнения типа ax^2 + bx + c = 0,
на вход принимается 3 числа, выводиться в консоль корни уравнения.
Решение квадратного уравнения см. здесь https://youclever.org/book/kvadratnye-uravneniya-1
"""

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


def root():  # функция вычисления корней при b!=0 и c!=0
    discriminant = pow(b, 2) - 4 * a * c  # вычисление дискриминанта D = b^2 -4ac
    if discriminant > 0:
        root_1 = int((- b - sqrt(discriminant)) / 2 * a)  # вычисление корней x = (-b +- sqrt(D)) / 2a
        root_2 = int((- b + sqrt(discriminant)) / 2 * a)
        print(root_1)
        print(root_2)
    elif discriminant == 0:
        root_1 = int((b * (-1)) / 2 * a)
        print(root_1)
    else:
        print("У квадратного уравнения нет корней")


if a == 0 and b == 0 and c == 0:
    print("У квадратного уравнения нет корней, введите числа отличные от нуля")
elif a != 0 and b != 0 and c != 0:
    root()
elif b == 0 and c != 0:
    if ((c * (-1)) / a) < 0:
        print("У квадратного уравнения нет корней")
    else:
        root_1 = int(sqrt(abs(c) / a)) * (-1)
        root_2 = int(sqrt(abs(c) / a))
        print(root_1)
        print(root_2)
elif b != 0 and c == 0:
    root_1 = 0
    root_2 = int(b / a) * (-1)
    print(root_1)
    print(root_2)
elif a != 0 and b == 0 and c ==0:
    root_1 = 0
    print(root_1)




