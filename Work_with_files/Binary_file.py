import pickle
import shelve

"""
fileName = 'users.dat'

name = 'Tom'
age = 16

with open(fileName, 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(fileName, 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print('Имя:', name, '\tВозраст:', age)
"""

"""
fileName = 'states'

with shelve.open(fileName) as file:
    file['London'] = 'Great Britan'
    file['Moskva'] = 'Russian'
    file['Vashington'] = 'USA'
    file['Berlin'] = 'Germany'

with shelve.open(fileName) as file:
    state = file.get('Paris', 'Not found')
    print(state)
    print(file['London'])
    print(file['Berlin'])
"""

fileName = 'states'

with shelve.open(fileName) as file:
    file['London'] = 'Great Britan'
    file['Moskva'] = 'Russian'
    file['Vashington'] = 'USA'
    file['Berlin'] = 'Germany'

with shelve.open(fileName) as file:
    for city in file.keys():
        print(city, end=' ')
    print()
    for state in file.values():
        print(state, end=' ')
    print()
    for state in file.items():
        print(state, end=' ')