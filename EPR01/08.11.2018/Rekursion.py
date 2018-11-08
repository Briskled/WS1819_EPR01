# Definition einer Rekursion:
# Eine Funktion ist rekursiv, wenn sie sich selbt aufruft.
# Hierbei entstehen sehr schnell endlos rekursive Schleifen.
# Diese können durch einfache if-Abfragen abgefangen werden


# Negativbeispiel: Diese Funktion berechnet zwar das gewünschte, aber die Laufzeit ist schrecklich.
# Sie berechnet bis zu 2**n zwischenergebnisse.
# Schon die 10. Fiboncci-Zahl braucht ca. 1024 Funktionsaufrufe.
def fibonacci(n):
     """Docstring: Berechnet den Wert der n-ten fibonacci Zahl.
     """
     if n == 1:
          return 1
     if n == 2:
          return 1
     return fibonacci(n-1) + fibonacci(n-2)



############### Fakultät durch Schleife berechnen ###############

n = int(input("Gib n ein >>> "))
fakultaet = 1
while n > 1:
     fakultaet *= n
     n -= 1
print("Durch Schleife: ", fakultaet)


def fak(n):
     """ Docstring: Berechnet n! (n-Fakultät)

     1! = 1
     n! = n * (n-1)!
     """
     if n < 0:
          print("Lauch")
          return 0
     if (n == 1):
          return 1
     return n * fak(n-1)

#5 * 4 * 3 * 2 * 1

     #n! = n * (n-1)!
     #5! = 5 * 4!
     #4! = 4 * 3!
     #3! = 3 * 2!
     #2! = 2 * 1!
     #1! = 1

n = int(input("Gib n ein >>> "))
print("Durch Rekursion: ", fak(n))
