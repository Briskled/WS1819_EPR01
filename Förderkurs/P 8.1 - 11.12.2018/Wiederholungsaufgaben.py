# Aufgabe 0 (zusammen):
# Welche Datenstrukturen kennst du? Und was sind überhaupt Datenstrukturen?

# Es gibt Datentypen und Datenstrukturen
# primitive Datentypen sind:
# - int
# - float
# - bool

# Datentypen, die "etwas" höher entwickelt sind
# - str

# Datenstrukturen
# - list
# - set
# - tuple
# - dictionary

# Aufgabe 1:
# Erstelle eine Liste mit dem Namen test aus Zahlen.
# Sie sollte mindestens 10 Elemente enthalten

test = [7,3,9,2,6,1,0,4,2,6,7,4,2]

# Aufgane 2:
# Iteriere mit einer for-Schleife über test und gib
# mit print jedes Element aus

for element in test:
     print(element)

# Aufgabe 3:
# Schreibe eine Funktion add, die zwei Argumente erwartet und
# die Summe beider Argumente
# zurückgibt

def add(a, b):
     c = a + b
     return c

variable1 = 1
variable2 = 5

add(variable1, variable2)

# Aufgabe 4:
# Schreibe ein Programm, welches den Benutzer zwei Zahlen eingeben lässt
# Benutze dafür zwei input-Anweisungen
# Anschließend sollen diese Zahlen mit der add-Funktion aus
# Aufgabe 2 addiert werden
# Lass das Ergebnis mit print ausgeben

zahl1 = input("Bitte geben Sie eine Zahl ein >>> ")
zahl2 = input("Bitte geben Sie noch eine Zahl ein >>> ")

if zahl1.isdigit() and zahl2.isdigit():
     zahl1 = int(zahl1)
     zahl2 = int(zahl2)
     c = add(zahl1, zahl2)
     print(c)
else:
     print("Falsche Eingabe(n)")


# Aufgabe 5:
# Schreibe ein Programm, welches den Benutzer einen Tiernamen eingeben lässt.
# Es soll zu jedem eingegebenen Tier dessen "Klasse" ausgeben.
# Beispiele:
# Benutzer sagt "Schwein". Programm antwortet "Säugetier"
# Benutzer sagt "Barsch". Programm antwortet "Fisch"
# Welche Datenstruktur verwendest du?

user_input = input("Gib einen Tiernamen ein >>> ")
classes = {"Schwein": "Säugetier", "Barsch": "Fisch", "Pandabär": "Säugetier",
           "Eule": "Vogel", "Faultier": "Säugetier", "Schlange": "Reptil"}


# Andersrum gehts auch
#animals = {"Säugetier": {"Faultier", "Pandabär", "Elefant"}}
#animals["Säugetier"]

# Aufgabe 6:
# Wie prüfst du, ob die Klasse eines eingegebenen Tieres überhaupt bekannt ist?
# Lasse "Nicht bekannt" ausgeben, wenn das eingegeben Tier nicht bekannt ist.

if user_input in classes:
     cls = classes[user_input]
     print(cls)
else:
     print("Nicht bekannt")













