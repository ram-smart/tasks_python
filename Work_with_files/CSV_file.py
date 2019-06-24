#! Чтение, запись фалов CSV (Comma Separated Values)

import csv # импорт модуля csv

fileName = 'users.csv'
users =[
    ['Tom', 25],
    ['Bill', 56],
    ['Alise', 18]
]

with open(fileName, 'w', newline='') as file: # newline='' для корректного считывания из файла вне зависимости от операц. системы
    writer = csv.writer(file)                 # создание объекта writer, вызывая csv.writer() из модуля csv передавая ему открытый файл file
    writer.writerows(users)

with open(fileName, 'a', newline='') as file:
    user = ['Sam', 45]
    writer = csv.writer(file)
    writer.writerow(user)

with open(fileName, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], ' - ', row[1])