# Wiederholungsfragen:

# Was ist eine Klasse? Was ein Objekt?
# Wozu verwendet man Attribute?
# Was ist der Unterschied zwischen Funktion und Methode?
# Schreibe eine Klasse >Animal< mit den Attributen >name< und >type<

class Animal:
     def __init__(self):
          self.name = "PLACEHOLDER"
          self.type = 0


def sum_first_n(n):
     flag = 1
     sum = 0
     while True:
          if flag <= n:
               sum += flag
               flag += 1
          else:
               return sum


def sum_first_n2(n):
     sum_n = 0
     while n > 0:
          sum_n += n
          n -= 1
     return sum_n


def sum_first_n3(n):
     sum_n = 0
     for i in range(n+1):
          sum_n += i
     return sum_n

# Aufgabe 1:
# Schreibe eine Funktion sum_firs_n(n), die die Summe der ersten n ganzen Zahlen
# berechnet und zurückgibt
# Wenn n=6 ist, soll sie also 1+2+3+4+5+6 berechnen


# Aufgabe 2 (vom Tutor):
# Schreibe eine REKURSIVE Funktion, die das gleiche tut wie sum_first_n(n)

def sum_rek(n):
     if n == 1:
          return 1
     else:
          return n + sum_rek(n-1)


# Aufgabe 3:
# Schreibe eine rekursive Funktion, die n! (Fakultät) berechnet.
# Wenn n=6 ist, soll sie also 6*5*4*3*2*1 berechnen

def fak(n):
     if n == 1:
          return 1
     else:
          return n * fak(n-1)

# Aufgabe 4 (vom Tutor):
# gegeben sei folgende rekursive Gleichung:
#   x(0) = 0
#   x(n) = 2*x(n-1) + 1
# Schreibe eine rekursive Funktion, die diese Gleichung implementiert


def task_4(n):
     if n == 0:
          return 0
     return 2*task_4(n-1) + 1


# Aufgabe 5:
# gegeben sei folgende rekursive Gleichung:
#   x(0) = 6
#   x(n) = x(n-1) + 3*x(n-1)
# Schreibe eine rekursive Funktion, die diese Gleichung implementiert

def task_5(n):
     if n == 0:
          return 6
     return task_5(n-1) + 3*task_5(n-1)

# Aufgabe 6:
# Die Berechnung für die n-te Fibonacci Zahl sieht so aus:
#   x(1) = 1
#   x(2) = 1
#   x(n) = x(n-1) + x(n-2)
# Schreibe eine rekursive Funktion, die diese Gleichung implementiert

def fib(n):
     if n == 1 or n == 2:
          return 1
     return fib(n-1) + fib(n-2)

# Aufgabe 7:
# Berechne mit deinem Programm die 4-te, 5-te, 10., 20. 30., 35. und 40. Fibonaccizahl.
# Was fällt dir auf?
# Warum ist das so?



# Freiwillige Hausaufgabe:
# Schreibe eine Funktion, die die n-te fibonnaci-Zahl berechnet, ohne dass es zu Laufzeitproblemen kommt
# Am besten mit fib(40) testen
# Muss nicht rekursiv sein (kann aber ;) )






