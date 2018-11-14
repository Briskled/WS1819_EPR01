

# Eine Liste mit den Elementen 5, 6, "Hi", ........
# Sie wird in der Variable a gespeichert
a = [5, 6, "Hi", 5.1, 1, "Hallo", 8, 6, 90, 10]

# Zählervariable
i = 0

# Schleife läuft von 0 bis kurz vor die Länge der Liste
while i < len(a):

     # Das i-te Element wird ausgegeben
     print(a[i])

     #Zähler erhöht
     i += 1



## ------- JETZT NOCHMAL MIT FOR-SCHLEIFEN -------- ##

# For durchläuft alle Elemente von a und merkt sich jedes element in der Variable "element"
for element in a:
     # gibt dieses Element aus
     print(element)


# Ein String ist auch nur eine Liste!!
# Alle Listenoperationen funktionieren auch mit Strings
variable = "Hallo Welt"
print(len(variable))
print(variable[4])
for element in variable:
     print(element)



# a[0:5] gibt eine neue Liste mit den Elementen an den Stellen 0, 1, 2, 3, 4 zurück.
# 5 ist nicht dabei!!!!!
print(a[0:5])

# Ganze liste:
print(a[0:len(a)])

# Ganze liste ohne das letzte Element
print(a[0:len(a)-1])

# Das gleiche:
print(a[0:-1])

# Ganze liste ohne die hinteren beiden Elemente
print(a[0:-2])

# Leere Liste:
b = []

# 5 ans Ende von b hängen
b.append(5)

# 6 ans Ende von b hängen
b.append(6)

# Die komplette Liste a ans Ende von b hängen
b.extend(a)
print("b =", b)

# Liste umdrehen
b.reverse()
print("b =", b)

# Overkill
# Dreht die Liste um, nimmt sich nur die vorhere Hälfte und dreht diese auch nochmal um
c = b[::-1][0:len(b)//2][::-1]
print("c =", c)
print("b =", b)



# Bonusaufgabe :D
# Python zeit messen googlen und programmieren.
# Was dauert länger? Sortieren oder mit for schleife das Minimum finden?
# Tipp: Nimm größere Listen




# Findet das kleinste Element in der Liste "zahlen"
zahlen = [5, 6, 7, 8, 4, 3, 2, 9, 10, 1, 11]
zahlen.sort()
print(zahlen[0])


# Macht das gleiche
minimum = zahlen[0]
for element in zahlen:
     if element < minimum:
          minimum = element
print(minimum)









