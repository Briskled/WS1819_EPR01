"""Docstring: Irgend eine Beschreibung"""

__author__ = "123456: Felix Lapp"
__credits__ = ""
__email__ = ""

def main():
     """Docstring: Main-Funktion"""
     pass




# Bei diesen Aufgaben werden Sets behandelt
# Außerdem wird geübt, anhand einer Beschreibung, eine Funktion zu bauen


# Aufgabe 1
# Schreibe das "Grundgerüst" eines Moduls
# Dazu gehhört:
#    - Main-Funktion
#    - Header
#    - Aufruf der Main-Funktion
#    - Docstring des Moduls
#    - Docstring der Main-Funktion

# Aufgabe 2
# Schreibe eine Funktion, die einen string A erwartet
# Sie soll "pong" als zurückgeben, wenn A "ping" ist
# Ansonsten soll sie None zurückgeben

def task_2(A):
     if A == "ping":
          return "pong"
     else:
          return None

# Aufgabe 3
# Schreibe eine Funktion, die ein Set S erwartet.
# Sie soll die Funktion aus Aufgabe 2 für jedes Element in S aufrufen
# und den zurückgegebenen Wert mit print ausgeben


def task_3(S):
     for element in S:
          print(task_2(element))



# Aufgabe 4
# Lasse die Main-Funktion die Funktion aus Aufgabe 3 aufrufen
# Benutze als Argument das Set {"String", "Ping", "Strong", "Pong", "string", "ping"}

# Aufgabe 5
# Schreibe eine Funktion, die den Benutzer genau 5 Strings eingeben lässt

# Aufgabe 6
# Modifiziere die Funktion aus Aufgabe 5 so, dass jeder eingegebene String
# zu einem Set hinzugefügt wird, sodass nach den Eingaben das Set genau 5 Werte hat.
# Die Funktion soll dieses Set zurückgeben

# Aufgabe 7
# Lasse die Main-Methode zuerst die Funktion aus Aufgabe 5/6 aufrufen
# Anschließend soll die Funktion aus Aufgabe 3 mit dessen Ergebnis
# aufgerufen werden.



if __name__ == "__main__":
     main()
