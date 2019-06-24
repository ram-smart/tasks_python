#! Запись и чтение словаря
import csv

fileName = 'dictionary.csv'

users = [
    {'name': 'Tom', 'age': 19},
    {'name': 'Bil', 'age': 25},
    {'name': 'Alise', 'age': 18}
]

with open(fileName, 'w', newline='') as file:
    columns = ['name', 'age']
    writer = csv.DictWriter(file, fieldnames=columns) # fieldnames= collumns наименование столбцов
    writer.writeheader() # запись заголовка
    writer.writerows(users) # запись нескольких строк

    user = {'name': 'Sam', 'age': 45}
    writer.writerow(user)

with open(fileName, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], ' - ', row['age'])
