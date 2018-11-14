__author__ = "123457: Felix Lapp"

n = 3
m = 6

counter = 0
i = 0
while i < n:
     #print("Äußere Schleife Durchlauf:", i)

     j = 0
     while j < m:
          #print("Innere Schleife Durchlauf:", j)
          print(i, j)
          summe = i + j

          #summe % 3 == 0 prüft, ob summe durch 3 teilbar ist

          # True wenn summe durch drei oder vier teilbar ist
          if(summe % 3 == 0 or summe % 4 == 0):
               print("Stimmt. Counter erhöhen")
               counter += 1
          j += 1

     
     i += 1
print("Counter:", counter)

     #0 % 3 = 0
     #1 % 3 = 1
     #2 % 3 = 2
     #3 % 3 = 0
     #4 % 3 = 1




################# Aufgaben!!! ################
#
# 1. Schreibe eine while-Schleife, die exakt 5 mal durchläuft und
#    insgesamt 5 mal "Hallo Welt" ausgibt
#
# 2. Schreibe eine while-Schleife, die n mal durchläuft. Der Benutzer bestimmt n.
#    In jedem Schleifendurchlauf wird "Hallo Welt 2" ausgegeben
#
# 3. Schreibe eine while-Schleife, die immer wieder den Benutzer eine Zahl eingeben lässt.
#    Sie bricht erst ab, wenn er 42 eingibt.
#
# 4. Modifiziere das Programm aus 3. so, dass jede Benutzereingabe in einer
#    Liste gespeichert wird.
#    As Ende einer liste LISTE lässt sich mit LISTE.append(ZAHL) die ZAHL anfügen
#
# 5. Modifiziere das Programm aus 4. so, dass nachdem abgebrochen
#    wurde, das Minimum von LISTE errechnet wird
#    Beispiel: Der Benutzer gibt 5, 6, 3, 9, 12, 76 und am Ende 42 ein. Dann steht in LISTE:
#         [5, 6, 3, 9, 12, 76]
#    Anschließend wird das Maximum 76 gefunden
# 6. Benutze:
#         coole_liste = [6, 98, 5, 10, 3, 96, 555, 42, 1337, 16, 32, 64]
#    Schreibe ein Programm, welches in aufsteigender Reihenfolge die Listenelemente ausgibt.
#    Also 3, 5, 6, 10, 16, 32, ......













