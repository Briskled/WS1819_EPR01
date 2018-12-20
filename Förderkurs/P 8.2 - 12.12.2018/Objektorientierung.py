# Aufgabe 1:
# Erstelle eine Klasse >Plant<.
#   sie speichert ein bool >is_blooming<, welches angibt,
# ob sie blüht oder nicht. is_blooming ist standardmäßig
# False

class Plant:
     """Class representing a plant"""

     def __init__(self):
          """Initializes an object"""
          self.is_blooming = False

          # __height ist eine ganz normale variable, die aber nicht von
          # außen gesehen werden kann. Damit kann sie nicht gelesen oder
          # geändert werden
          self.__height = 0

     def grow(self):
          """Docstring: increases the height. If height reaches 5 it starts to bloom"""
          self.__height = self.__height + 1
          if self.__height >= 5:
               self.is_blooming = True


     # Getter für das Attribut __height
     def get_height(self):
          """Docstring: Gets the height of the plant"""

          # __height ist ja privat. Deshalb kann ohne getter nicht drauf zugegriffen werden
          return self.__height

     # Setter für das Attribut __height
     def set_height(self, height):
          self.__height = height
          if self.__height >= 5:
               self.is_blooming = True




# Aufgabe 2:
# Füge ein Attribut >height< hinzu, welches angibt,
# wie groß die Pflanze ist.
# Es soll standardmäßig 0 sein

# Aufgabe 3:
# Füge eine Methode >grow< hinzu. Sie soll >height< um
# 1 erhöhen

# Aufgabe 4:
# Erstelle zwei Objekte >plant1< und >plant2< der Klasse Plant.
# Rufe die
# grow-Methode von >plant1< auf.

# Zwei Objekte der Klasse Plant erstellen
plant1 = Plant()
plant2 = Plant()

plant1.grow()
print("Pflanze 1 ist jetzt", plant1.get_height(), "cm groß und blüht:", plant1.is_blooming)
plant1.set_height(20)
print("Pflanze 1 ist jetzt", plant1.get_height(), "cm groß und blüht:", plant1.is_blooming)
print("Pflanze 2 ist jetzt", plant2.get_height(), "cm groß und blüht:", plant2.is_blooming)
# Aufgabe 5:
# Lasse mit print die Höhen beider Pflanzenobjekte ausgeben


# Methode = Funktion










