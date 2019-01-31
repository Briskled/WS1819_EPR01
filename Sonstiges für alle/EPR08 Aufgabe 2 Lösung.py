# Header...
import math
import random

#  1 1 2 3 5 8 13 21
#  a b
#    a b
#      a b
#        a b


class Fibonacci:

     def iterativ_fib(self, n):
          a = 1
          b = 1
          for i in range(n-1):
               a = a + b
               b, a = a, b
               
          return a
               

     def rekursiv_fib(self, n):
          if n == 1 or n == 2:
               return 1

          return self.rekursiv_fib(n-1) + self.rekursiv_fib(n-2)


     def rekursiv_fib_better(self, m, a=1, b=1):
          if m == 1:
               return a
          return self.rekursiv_fib_better(m-1, b, a + b)


#   8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
#       7 * 6 * 5 * 4 * 3 * 2 * 1
class Fakultaet:

     def iterativ_fak(self, n):
          product = 1
          for i in range(1, n+1):
               product *= i
          return product

     def rekursiv_fak(self, n):
          if n == 1:
               return 1
          return n * self.rekursiv_fak(n-1)


class Unterklasse(Fibonacci, Fakultaet):

     klassenvariable = 0

     def __init__(self):
          n = int(input("Positive ganze Zahl eingeben >>> "))

          self.amount_rek_fib = 0
          self.amount_iter_fib = 0
          self.amount_rek_fak = 0
          self.amount_iter_fak = 0

          if n % 2 == 0:
               erg = self.rekursiv_fib(n)
          else:
               erg = self.iterativ_fak(n)

          for i in range(1000):
               erg = self.noise_me(erg)

          print("Anzahl Rek Fib:", self.amount_rek_fib)
          print("Anzahl Iter Fib:", self.amount_iter_fib)
          print("Anzahl Rek Fak:", self.amount_rek_fak)
          print("Anzahl Iter Fak:", self.amount_iter_fak)
          

     def noise_me(self, erg):

          
          string = str(erg)
          D = 0
          for ziffer in string:
               ziffer_int = int(ziffer)
               D += ziffer_int
          D /= len(string)
          D = math.ceil(D)

          if D % 2 == 0: #ist grade
               # fibonacci
               rand = random.randint(0, 1)
               if rand == 1:
                    erg = self.iterativ_fib(D)
                    self.amount_iter_fib += 1
               else:
                    erg = self.rekursiv_fib(D)
                    self.amount_rek_fib += 1
          else:
               # fakultät
               rand = random.randint(0, 1)
               if rand == 1:
                    erg = self.iterativ_fak(D)
                    self.amount_iter_fak += 1
               else:
                    erg = self.rekursiv_fak(D)
                    self.amount_rek_fak += 1
                    
          return erg
          

def test(n):
     """Zum testen wie hoch die Rekursionstiefe ist"""
     print(n)
     test(n+1)


u = Unterklasse()
v = Unterklasse()

if __name__ == "__main__":
     main()










