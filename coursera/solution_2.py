import sys
""" Рисуем лестницу. В командной строке в качестве аргумента принимается 
целое число - количество ступеней. Программа выводит в консоль пробелы и 
решетки образуюя лестницу
"""
# моя версия
num_steps = int(sys.argv[1])
i = 0
for steps in range(num_steps):
    i += 1
    print(" " * (num_steps - i) + "#" * i)


# версия Coursera
num_steps = int(sys.argv[1])

for i in range(num_steps):
    print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")
