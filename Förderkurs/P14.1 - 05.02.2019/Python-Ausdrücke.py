def f(n):
     summ = 0
     for i in range(n):
          summ += 2*i + 1
     return summ


def g(lst):
     for i in range(len(lst)):
          lst[i] *= i
     return lst


def h(num):
     for i in range(2, int(num**0.5)):
          if num % i == 0:
               return False
     return True

# a)   True, wenn num durch jedes i teilbar ist
# b)   True, wenn num mindestens einen Teiler hat
# c)   True, wenn num eine Primzahl ist


def k(lst, t):
     summ = 0
     for i in lst:
          summ += i
     return summ % t == 0
