#with open('hello.txt', 'w') as file:
#   file.write('Чтобы открыть текстовый файл на запись, необходимо применить')

#with open('hello.txt', 'a') as file:
#    file.write(' режим w (перезапись) или a (дозапись).')

#with open('hello.txt', 'a') as file:
#    print('Дозапись выглядит как добавление строку', file = file)

"""
with open('hello.txt', 'r') as file:
    #s = file.read()
    s1 = file.readline()
    print(s1, end='')
"""
"""
with open('hello.txt', 'r') as file:
    for line in file:
        print(line, end='')
"""

"""
with open('hello.txt', 'r') as file:
    s = file.readlines()
    print(s)
    print(type(s))

"""

"""
file_name = 'hello.txt'
with open(file_name, encoding='utf8') as file:
    text = file.read()
"""
"""
#! Считывание, запись и вывод данных из файла

fileName = 'List'
spisok = list()

for i in range(4):
    item = input('Введите строку ' + str(i + 1) + ': ')
    spisok.append(item + '\n')

with open(fileName, 'w') as file:
    for i in spisok:
        file.write(i)

print('Считанные строки')
with open(fileName, 'r') as file:
    for i in file:
        print(i, end='')
"""