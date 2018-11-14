# Gibt die ersten 10 Quadratzahlen aus. Beginnend bei 0 und Ende bei 9
for x in range(10):
     print(x**2)


# Gibt die Elemente der Liste [1, 6, 2, 5] untereinander aus
for y in [1, 6, 2, 5]:
     print(y)


# pass ist dafür da, einen Rumpf zu füllen, ohne etwas zu tun.
# einfach nur
# if 5 == 5:
# else:
#    print("Hi")
# gäbe einen Fehler
if 5 == 5:
     pass
else:
     print("Hi")

# Soll auch die ersten 10 Quadratzahlen ausgeben.
# Falls aber eine Zahl gerade ist wird sie übersprungen mit continue
for x in range(10):
     if x % 2 == 0:
          continue
     print(x**2)



