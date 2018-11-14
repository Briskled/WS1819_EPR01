__author__ = "123456: Felix Lapp"


#Präsenzblatt Wiederholungsaufgabe 1

n_str = input("Gib ma bitte n ein: ")
n = eval(n_str)
Z = (n**2-n)/2
print(Z)




#Präsenzblatt Wiederholungsaufgabe 2:

(23 - (5 + 2**2 * 2)) * 5 // (5**2) - 4**0
(23 - (5 + 4 * 2)) * 5 // (5**2) - 4**0
(23 - (5 + 8)) * 5 // (5**2) - 4**0
(23 - 13) * 5 // (5**2) - 4**0
10 * 5 // (5**2) - 4**0
10 * 5 // 25 - 4**0
50 // 25 - 1
2 - 1
1





d = input("Gib was ein")
# Wir wollen prüfen, ob d eine ganze Zahl ist
# d ist eigentlich ein string (weil input immer einen string zurückgibt)

d.isdigit()
# das liefert True, wenn in d tatsächlich eine Zahl steht. Z.B. "6" oder "89"

eval(d) is int
# eval errechnet den Wert von d mit dem richtigen Datentypen.
# wenn also d tatsächlich eine Zahl ist, dann hat eval(d) auch den Datentyp int
# mit    is int    kann dann geprüft werden, ob es ein int ist
# geht auch mit   is float   sowie mit allen anderen Datentypen.

print(type(eval(d)))
# das printet den Datentyp von d





# Vergleichsoperatoren
# a == b            prüft, ob a und b absolut identisch sind
# a < b             prüft, ob a kleiner ist als b
# a > b             prüft, ob a größer ist als b
# a <= b            prüft, ob a kleiner oder gleich ist als b
# a >= b            prüft, ob a größer oder gleich ist als b
# a != b            prüft, ob a nicht das gleiche ist wie b

# In jedem Fall kommt entweder True oder Flase raus






