import json
import os
import argparse
'''
это скрипт, который принимает в качестве аргументов ключи и значения и выводит информацию из хранилища
Запись значения по ключу $: key_value_storage_my_version.py --key key_name --val value
Получение значения по ключу $: storage.py --key key_name
Ответом в данном случае будет вывод с помощью print соответствующего значения $: value
или $: value_1, value_2
если значений по этому ключу было записано несколько. 
Если значений по ключу не было найдено, выводит пустую строку или None. Данные хранит в формате JSON.
'''
parser = argparse.ArgumentParser()
parser.add_argument("--key", help="dictionary key")
parser.add_argument("--val", help="the value of the dictionary key")
args = parser.parse_args()

if args.key != None and args.val != None:
    if os.path.exists('storage.txt') is False:
        storag = dict()
        storag[args.key] = args.val
        file = open('storage.txt', mode='w', encoding='utf8')
        json.dump(storag, file)
        file.close()
    elif os.path.exists('storage.txt') and os.stat('storage.txt').st_size == 0:
        storag = dict()
        storag[args.key] = args.val
        file = open('storage.txt', mode='a', encoding='utf8')
        json.dump(storag, file)
        file.close()
    elif os.path.exists('storage.txt') and os.stat('storage.txt').st_size != 0:
        file = open('storage.txt', mode='r', encoding='utf8')
        dict_from_file = json.load(file)
        file.close()
        if args.key in dict_from_file:
            if type(dict_from_file[args.key]) == list:
                dict_from_file[args.key].append(args.val)
            else:
                list_values = []
                list_values.append(dict_from_file[args.key])
                list_values.append(args.val)
                dict_from_file[args.key] = list_values
        else:
            dict_from_file[args.key] = args.val
        file = open('storage.txt', mode='w', encoding='utf8')
        json.dump(dict_from_file, file)
        file.close()
elif args.val == None:
    if os.path.exists('storage.txt') == False:
        print("Файла не существует, введите данные (--key key_name --val value) для создания файла")
    else:
        file = open('storage.txt', mode='r', encoding='utf8')
        dict_from_file = json.load(file)
        if args.key in dict_from_file and type(dict_from_file[args.key]) == list:
            list_values = dict_from_file[args.key]
            print(', '.join(map(str, list_values)))
        elif args.key in dict_from_file:
            print(dict_from_file[args.key])
        elif args.key not in dict_from_file:
            print("None")