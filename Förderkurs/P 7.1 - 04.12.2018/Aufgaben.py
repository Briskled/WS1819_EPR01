# Es soll ein Roboterduell stattfinden!
# Vier Roboter treten jeweils in Zweikämpfen gegeneinander an.
# Jeder Roboter hat einen Namen, eine Größe, und einen Kampfwert.

# Magnetron ist 3.5 Meter groß und hat einen Kampfwert von 9
# Der Robostampf ist 6 Meter groß und hat einen Kampfwert von 17
# Saboteur ist 0.5 Meter groß und hat einen Kampfwert von 11
# Staubsauger 3000 ist 0.3 Meter groß und hat einen Kampfwert von 1

KEY_HEIGHT = "größe"
KEY_NAME = "name"
KEY_VALUE = "kampfwert"


# Aufgabe 1:
# Plane, wie du diese Informationen am geschicktesten in einem
# Python-Modul implementiert

# Aufgabe 2:
# Setze deine Planung um
def who_wins(robo1, robo2):
     if robo1[KEY_VALUE] > robo2[KEY_VALUE]:
          print(robo1[KEY_NAME] + " gewinnt")
     elif robo1[KEY_VALUE] == robo2[KEY_VALUE]:
          print("Unentschieden")
     else:
          print(robo2[KEY_NAME] + " gewinnt")

# Aufgabe 3:
# Zuerst treten Magnetron und Saboteur gegeneinander an.
# Schreibe ein Programm, das errechnet, wer gewinnt

# Aufgabe 4:
# Nun tritt der Robostampf gegen den Staubsauger 3000 an.
# Schreibe auch hier ein Programm, das errechnet, wer gewinnt

# Aufgabe 5:
# Modifiziere das Programm nun so, dass der Benutzer die vier
# Kampfwerte per input auswählen kann.
# Programmiere es robust!!

# Aufgabe 6:
# Musst du deine Lösungen für Aufgabe 3 und 4 jetzt anpassen?
# Falls ja: tu es

# Aufgabe 7:
# Ergänze nun einen Codeabschnitt, der den Roboter
# mit dem höchsten Kampfwert findet und seinen Namen ausgibt.
