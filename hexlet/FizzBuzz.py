def fizz_buzz(begin, end):
    if begin > end:
        return ''

    result = ''
    for i in range(begin, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            result = result + 'FizzBuzz '
        elif i % 3 == 0:
            result = result + 'Fizz '
        elif i % 5 == 0:
            result = result + 'Buzz '
        else:
            result = result + str(i) + ' '

    return '{0}'.format(result.rstrip())
