# Рекурсия
# https://ru.hexlet.io/courses/introduction_to_programming/lessons/iterative/exercise_unit#theory

# Рекурсивный процесс
def factorial (n):
  if n == 2:
      return n
  else:
      return n + factorial(n - 1)


def Sum (n1, n2):
  if n2 == n1:
      return n2
  elif n2 < n1:
      return n2 + Sum(n1, n2 + 1)
  else:
      return n2 + Sum(n1, n2 - 1)


# Итеративный процесс
def SunIterativ(n):
    def iter(counter, acc):
        if counter == 1:
            return acc
        return iter(counter - 1, counter * acc)

    return iter(n, 1)

# Нахождение наименьшего делителя заданного числа с помощью итертативного процесса

def smallestDevisor(n):
    if n == 0:
        return 0
    def devisor(n, acc):
        if n == 1:
            return acc
        if (n % (acc + 1)) == 0:
            return acc + 1
        return devisor(n, acc + 1)
    return devisor(n, 1)


print(smallestDevisor(2))


#print(Sum(-5, 4))
#print(factorial(6))
#print(SunIterativ(5))
