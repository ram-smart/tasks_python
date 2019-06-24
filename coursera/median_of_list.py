import random
import statistics

"""
программа выводит в консоль отсортированный список целых чисел,
длину списка и среднее значение.
"""
numbers = []
numbers_size = random.randint(15, 20)

for _ in range(numbers_size):
    numbers.append(random.randint(1, 50))

numbers.sort()
print("отсортированный список ", numbers)
print("длина списка ", len(numbers))
print("среднее значение statistics ", statistics.median(numbers))

if len(numbers) % 2 == 0:
    numb_1 = numbers[int(len(numbers) / 2)]
    numb_2 = numbers[int(len(numbers) / 2) - 1]
    median_number = (numb_1 + numb_2) / 2
    print("среднее значение ", median_number)
else:
    median_number = numbers[(len(numbers) // 2)]
    print("среднее значение ", median_number)