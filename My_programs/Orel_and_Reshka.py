from random import randrange

x = 'y'
while x == 'y':
    print('Программа \'Орел и решка\'', '\n'
          'Введите кол-во подбрасываний монеты')
    n = int(input())
    numbers = [randrange(0, 2) for i in range(n)]
    c0 = numbers.count(0)
    c1 = numbers.count(1)
    percent_c0 = round(c0 * 100 /n, 2)
    percent_c1 = round(c1 * 100 /n, 2)
    if percent_c0 > percent_c1:
        print('Выпал \'Орел\'')
    else:
        print('Выпал \'Решка\'')
    print(#'Список ', numbers, '\n',   # 0 - орел, 1 - решка
        'Кол-во 0 ', c0,'\n',
        'Кол-во 1 ', c1, '\n' 
        'Процент выпадения \'Орел\' ', percent_c0, '\n'
        'Процент выпадения \'Решка\' ', percent_c1, '\n')

    print('Хотите продолжить? Если да введите \'Y\' если нет \'N\'')
    x = input().lower()
print('Программа завершена')