# Eine while-Schleife, die genau n mal läuft

n = 10 # hier kann jede positive natürliche Zahl stehen
while n > 0:
     # Hier werden dann eine oder mehrere beliebige Anweisungen stehen.
     # Beispielsweise print
     n -= 1




# Eine for-Schleife, die genau n mal durchläuft
for i in range(n):
     # Hier steht dann eine Anweisung.
     # Beachte, dass i mit 0 beginnt und mit 9 endet.
     pass



# Beispiele:


#Summe der ersten n Zahlen
summe = 0
n = 10 # wieder beliebig
while n > 0:
     summe += n
     n -= 1
print(summe)


# Summe der ersten n Zahlen mit einer for-Schleife
n = 10
summe = 0
# bei range(n)  ist das Element n nicht mehr dabei.
# Deshalb müssen wir 1 addieren, damit es doch dabei sit
for i in range(n+1):
     summe += n
print(summe)



# Summe der ersten n Quadratzahlen
n = 10
summe = 0
for i in range(n+1):
     summe += i**2








