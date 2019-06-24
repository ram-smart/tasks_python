import json
import os
import argparse
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="dictionary key")
parser.add_argument("--val", help="the value of the dictionary key")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.key != None and args.val != None:  # блок if для внесения данных в файл
    if os.path.exists('storage_path') is False:
        new_dict = dict()
        new_dict[args.key] = args.val
        with open('storage_path', mode='w', encoding='utf8') as file:
            json.dump(new_dict , file)
    elif os.path.exists('storage_path') and os.stat('storage_path').st_size == 0:
        new_dict = dict()
        new_dict[args.key] = args.val
        with open('storage_path', mode='a', encoding='utf8') as file:
            json.dump(new_dict, file)
    elif os.path.exists('storage_path') and os.stat('storage_path').st_size != 0:
        with open('storage_path', mode='r', encoding='utf8') as file:
            dict_from_file = json.load(file)
        if args.key in dict_from_file and type(dict_from_file[args.key]) == list:
            dict_from_file[args.key].append(args.val)
        elif args.key in dict_from_file and type(dict_from_file[args.key]) != list:
            list_values = []
            list_values.append(dict_from_file[args.key])
            list_values.append(args.val)
            dict_from_file[args.key] = list_values
        else:
            dict_from_file[args.key] = args.val
        with open('storage_path', mode='w', encoding='utf8') as file:
            json.dump(dict_from_file, file)
elif args.val == None:  # блок elif для вывода значения по ключу
    with open('storage_path', mode='r', encoding='utf8') as file:
        dict_from_file = json.load(file)
        if args.key not in dict_from_file:
            print('')
        else:
            with open('storage_path', mode='r', encoding='utf8') as file:
                dict_from_file = json.load(file)
            if args.key in dict_from_file and type(dict_from_file[args.key]) == list:
                list_values = dict_from_file[args.key]
                print(', '.join(map(str, list_values)))
            elif args.key in dict_from_file:
                print(dict_from_file[args.key])
            elif args.key not in dict_from_file:
                print('')