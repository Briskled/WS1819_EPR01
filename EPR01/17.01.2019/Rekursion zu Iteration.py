

def fib(n):
     if n == 1 or n == 2:
          return 1
     return fib(n-1) + fib(n-2)



def fib_iter(n):
     a = 1
     b = 1
     c = 0
     for i in range(n-2):
          c = a + b
          a = b
          b = c
     return c
