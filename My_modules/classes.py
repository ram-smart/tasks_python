class Person:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone
    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone):
        if int(phone):
            self.__phone = phone
        else:
            print('Error')

    def display_info(self):
        print('Имя: %s \tТелефон: %d' % (self.__name, self.__phone))

class Auto:
    def __init__(self, auto_name, speed):
        self.__autoName = auto_name
        self.__speed = speed

    def display_info(self):
        print('Авто %s \tедет со скоростью: %s км/ч' % (self.__autoName, self.__speed))

class Employee (Person):
    def __init__(self, name, phone, company):
        Person.__init__(self, name, phone)
        self.company = company

    def display_info(self):
        Person.display_info(self)
        print('Работает в компании ', self.company)

class Student (Person):
    def __init__(self, name, phone, university):
        Person.__init__(self, name, phone)
        self.university = university

    def display_info(self):
        print('Студент %s, тел. %d, учиться в %s' % (self.name, self.phone, self.university))

"""
people = [Person('Tom', 111111), Employee('Alise', 22222, 'Google'), Student('Bob', 333333, 'МГУ')]
for person in people:
    person.display_info()
    print()

for person in people:
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
    print()
"""