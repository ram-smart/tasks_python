def cons(a, b):
    return lambda message: {message == 'a': a, message == 'b': b}.\
        get(True, "Неверный ключ")


def car(pair):
    return pair('a')


def cdr(pair):
    return pair('b')


def function():
    pass