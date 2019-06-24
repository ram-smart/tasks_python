stroka = 'cxzkvjnhsxvnjshdfkafpeotpeorypethlgbnsdhkgokhdfblsdf'
spisok = list(stroka)
print(spisok)

dictionary = dict()

for symbol in spisok:
    if symbol in dictionary:
        dictionary[symbol] = dictionary[symbol] + 1
    else:
        dictionary[symbol] = 1

for key, value in dictionary.items():
    print(key, ' - ', value)

with open('dict_file.txt', 'w') as file:
    for key, value in dictionary.items():
        s = key + ' - ' + str(value) + '\n'
        file.write(s)
        print('\n')