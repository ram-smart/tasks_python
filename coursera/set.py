import random

"""
через какое количество итерация будет повтор
"""

random_set = set()

while True:
    new_number = random.randint(1, 10)
    if new_number in random_set:
        break

    random_set.add(new_number)

print(random_set)
print(len(random_set) + 1)  # "+ 1" т.к. на последней итерации число не добавиться в множество