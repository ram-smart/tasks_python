
'''
storage_path = os.path.join(tempfile.gettempdir(), 'storage_data')
file = open(storage_path, mode='a', encoding='utf8')
json.dump(storage_dict, file)
file.close()

file = open(storage_path, mode='r', encoding='utf8')
key_value = json.load(file)
print(key_value)
file.close()
'''

spisok = [1, 2, '3', 5]
for x in spisok:
    print(*spisok, sep=", ")
