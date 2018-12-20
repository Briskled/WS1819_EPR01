"""Krasses Denglisch"""

class Essen:
     """Abstract Class representing Food"""

     def __init__(self):
          """Constructor"""
          
          self.__kalorien = 0
          self.__geschmack = 0

     def get_kalorien(self):
          """Getter for attribute kalorien"""
          return self.__kalorien

     def set_kalorien(self, kalorien):
          """Setter for attribute kalorien"""
          self.__kalorien = kalorien

     def get_geschmack(self):
          """Getter for attribute geschmack"""
          return self.__geschmack

     def set_geschmack(self, geschmack):
          """Setter for attribute geschmack"""
          if geschmack < 0:
               self.__geschmack = 0
          elif geschmack > 10:
               self.__geschmack = 10
          else:
               self.__geschmack = geschmack

     def unterschied_geschmack(essen1, essen2):
          print("Geschmack von Essen1:", essen1.get_geschmack())
          print("Geschmack von Essen2:", essen2.get_geschmack())
          unterschied = essen1.get_geschmack() - essen2.get_geschmack()
          print("Differenz:", unterschied)


class Wurst(Essen):
     """"""
     def __init__(self):
          """"""
          Essen.__init__(self)
          self.set_kalorien(600)

class Brokkoli(Essen):

     def __init__(self):
          Essen.__init__(self)
          self.set_geschmack(0)
     


b = Brokkoli()
b.set_kalorien(50)

w = Wurst()
w.set_geschmack(3)

Essen.unterschied_geschmack(b, w)

# Aufgabe 1:
# Implementiere die Klasse >Essen<
# Sie speichert zwei private Attribute:
# einen Kalorienwert und einen Wert zwischen 1 und 10, der den Geschmack angibt

# Aufgabe 2:
# Implementiere Getter und Setter für beide Attribute der Klasse >Essen<

# Aufgabe 3:
# Implementiere die Klasse >Wurst<. Sie soll von >Essen< erben
# Wurst soll im Konstruktor ihren eigenen Kalorienwert auf 600 setzen

# Aufgabe 4:
# Implementiere die Klasse >Brokkoli<. Sie soll auch von >Essen< erben
# Ihr Geschmackwert soll im Konstruktor auf 0 gesetzt werden

# Aufgabe 5:
# Implementiere eine Klassenfunktion, die zwei Objekte der Klasse Essen erwartet
# und die Differenz der Geschmackwerte ausgibt

# Aufgabe 6:
# Modifiziere den Setter von Geschmack so, dass keine Werte erlaubt sind, die kleiner als 0 oder
# größer als 10 sind.
# Werte kleiner 0 sollen automatisch auf 0 gesetzt werden. Werte größer 10 automatisch auf 10
