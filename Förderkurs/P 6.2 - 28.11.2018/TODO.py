# Aufgabe 1 (Wiederholung):
# Was ist der Unterschied zwischen Listen und Sets? Was sind die Gemeinsamkeiten?

s = {6,2,6,8,4,2,2}
#Leeres Set
s = set()

# Aufgabe 2 (Wiederholung):
# Was sind Dictionaries? Wofür kann man sie z.B: verwenden?


# Aufgabe 3 (Wiederholung):
# Wie erstelle ich ein leeres Dictionary?
# Wie füge ich ein Schlüssel-Wert-Paar hinzu?
# Wie finde ich den Wert zu einem Schlüssel heraus?
# Was passiert, wenn ich auf einen Schlüssel zugreife, der nicht existiert?

d = dict()
#oder
d = {}
d["Schlüssel"] = "Wert"
print(d.get("Schlüssel"))
print(d["Schlüssel"])
counter = 0
search_for = "Schlüssel"
for key in d:
     print(key)
     if key == search_for:
          break
     counter += 1

# KeyError wenn Schlüssel nicht existiert
# man sollte vorher prüfen, ob der Schlüssel existiert
if "Was anderes" in d:
     print(d["Was anderes"])  #wird nicht ausgeführt


# Aufgabe 4:
# Finde heraus, wie man am schnellsten aus einem Set eine Liste macht
# Geht das auch umgekehrt?

s = {1,6,2,5,3}
l = list(s)
print(s)
print(l)
s2 = set(l)
print(s2)

# Aufgabe 5:
# Schreibe ein Programm, welches die Liste [7,8,5,1,9,22,6,3] aufsteigend sortiert!
# Welche Probleme könnten hierbei auftreten?
# Wie könnte die Liste stattdessen absteigend sortiert werden?

list_to_sort = [7,8,5,1,9,22,6,3]
sorted_set = set(list_to_sort)
sorted_list = list(sorted_set)
sorted_list.reverse()         #dreht die Liste um
print(sorted_list)













