
# Entwerft ein dictionary, welches Informationen über euch selbst speichert:
#    - Körpergröße
#    - Name
#    - Fachsemester
#    - Geschlecht
#    - Anzahl der Haustiere

ich = {"Körpergröße" : 190,
       "Name" : "Felix Lapp",
       "Fachsemester" : 6,
       "Geschlecht" : "m",
       "Anzahl der Haustiere" : 0}


# Aufgabe 2:
# Was passiert, wenn man mit einer for-Schleife über ein Dictionary iteriert
#    Was ist denn überhaupt "iterieren"?

for i in ich:
     print(i)


# Aufgabe 3:
# Wie kann ich mit mithilfe einer for-Schleife alle Schlüssel und
# die dazugehörigen Werte
# anzeigen lassen?
print("\n")

for i in ich:
     print(i, ich[i])


# Aufgabe 4:
# Erstellt ein neues dictionary mit dem Namen test.
# Ein leeres dictionary erstellt man mit   test = {}        <- Geschweifte Klammern
# Einfügen geht mit:
#    test[schluessel] = wert
# Fügt ZUERST das Schlüssel-Wert-Paar   1 : "Erster"      ein
# ANSCHLIESSEND das Paar                8 : "Zweiter"
# ZULETZT das Paar                      10 : "Dritter"

test = {}
test[1] = "Erster"
test[8] = "Zweiter"
test[8] = "Vierter" #Überschreibt Zweiter
test[10] = "Dritter"

print(test)


# Aufgabe 5:
# Wie kann ich prüfen, ob ein bestimmter Schlüssel in einem
# dictionary vorhanden ist?

if 1 in test:
     print("Schlüssel vorhanden")
else:
     print("Schlüssel nicht vorhanden")

# Aufgabe 6:
# Schreibe ein Programm, welches alle Werte aus dem Dictionary
# aus Aufgabe 1 in einer Liste speichert

liste = []
for i in ich:
     liste.append(ich[i])
print(liste)


# Aufgabe 7:
# Erkundige dich, was ein Set ist

#Eine Mathetmatische Menge :D

# Aufgabe 8:
# Erstelle ein Set mit den Werten 9, 7, 2, 5, 4, 1  (in der Reihenfolge)
# Lass es dir ausgeben
# Was fällt dir auf?

ein_set = {9, 7, 2, 5, 4, 1, 6}
print(ein_set)

# Aufgabe 9:
# mit .add(WERT) kann WERT zum set hinzugefügt werden
# Was passiert, wenn 7 hinzugefügt wird?
# Lass es dir ausgeben

ein_set.add(7)
print(ein_set)










