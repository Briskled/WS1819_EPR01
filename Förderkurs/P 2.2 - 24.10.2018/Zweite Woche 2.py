__author__ = "123456: Felix Lapp"



# Präsenzübungsblatt 2 - Woche zwei
input1 = input("Gib etwas ein: ")
input2 = input("Gib noch etwas ein: ")
equal = input1 == input2
print(equal)



# Modifizieren, sodass der Benutzer drei Variablen eingibt
input1_string = input("Gib etwas ein: ")
input2 = input("Gib noch etwas ein: ")
input3 = input("Und noch was: ")

equal = input1 == input2 == input3
print(equal)



n = 3
while n > 0:
     eingabe = input("Gib Zahl Nummer "+str(4-n)+" ein")
     n -= 1







while True:
     print("Wie oft geprintet?")
     break                         # break unterbricht jede Schleife!
                                   # Wenn eine Schleife in einer Schleife ist wird nur die innere Unterbrochen







# Wenn eine Schleife 5 mal Ausgeführt werden soll
n = 1
while n < 6:
     print("Ausgeführt", n)
     n = n + 1
     if n < 3:
          break


print("\n\n")

# So macht man das normalerweise
n = 5
while n > 0:
     print("Ausgeführt", n)  
     n -= 1                          # n -= 1    ist das gleiche wie    n = n - 1
print("Außerhalb von while")





a = 6
b = 5

if a < b:
     print("A kleiner B")
elif a > b:
     print("A größer B")
else:
     print("A gleich B")
print("Das steht immer hier")





print("Es sollen die ersten n Zahlen addiert werden.")
n_str = input("Gib mir n! ")
if n_str.isdigit():                     # Wenn n_str eine Zahl ist wird weiter gemacht......
     n = int(n_str)
     summe = 0
     while n > 0:
          summe += n                    # Summe wird um n erhöht.
          n -= 1                        # n wird um eins verringert
                                        # Dadurch steht am Ende der Schleife die Summe von 1 bis n
                                        # 1 + 2 + 3 + 4 + 5 + ..... + (n-1) + n
     print(summe)
else:                                   # Wenn n_str keine Zahl ist kommt ein Error
     print("Lappen! Is keine Zahl!")



# n = 4
# summe = 0
# summe = 0 + 6
# summe = 0 + 6 + 5
# summe = 0 + 6 + 5 + 4 + 3 + 2 + 1




# Live Programming aus der Präsenzübung


# Endlos wiederholen
while True:
     eingabe1 = input("Gib die erste Zahl ein!")
     eingabe2 = input("Gib die zweite Zahl ein!")

     # Diese Bedingung ist genau dann erfüllt, wenn wirklich BEIDE eingaben ganze Zahlen sind
     if eingabe1.isdigit() and eingabe2.isdigit():

          #Variablen zu Integers machen
          a = int(eingabe1)
          b = int(eingabe2)

          
          if a > b:
               print("Erste Zahl ist größer")
          elif a < b:                                          # elif wird nur dann ausgeführt,
                                                               # wenn if a > b nicht ausgeführt wird
               print("Zweite Zahl ist größer")
          else:                                                # else wird nur dann ausgeführt,
                                                               # wenn weder if a > b noch elif a < b ausgeführt wurde
               print("Gleich und gleich gesellt sich gern")

          # wenn das alles erfolgreich ausgeführt
          # wurde wird die Schleife abgebrochen
          break
     else:
          # Error ausgeben. Die Schleife läuft weiter und damit kommt wieder eine Eingabe
          print("Error!")











