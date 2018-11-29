import sys
"""программа подсчета суммы цифр входящих в число. 
число передается как аргумент командной строки
"""
# моя версия
digit_string = sys.argv[1]
result = 0
for i in digit_string:
    result += int(i)
print(result)


# версия Coursera
print(sum([int(x) for x in sys.argv[1]]))