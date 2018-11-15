__author__ = "1234567: Felix Lapp"
#hier so credits und co




loop_type = input("Welchen Schleifentypen willst du benutzen ('for' oder 'while')? >>> ")
n_input = input("Gib mir n >>> ")
n = int(n_input)

if loop_type == "for":
     summe = 0
     for i in range(1, n+1):
          summe += i
     avr = summe / n
     print("Durchschnitt ist", avr)
elif loop_type == "while":
     summe = 0
     i = 1
     while i < n+1:
          summe += i
          i += 1
          #i = i + 1
     avr = summe / n
     print("Durchschnitt ist", avr)
else:
     print("Falsche Schleifenart")
