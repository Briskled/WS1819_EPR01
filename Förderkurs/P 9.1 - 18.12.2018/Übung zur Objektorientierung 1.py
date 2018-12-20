class Animal:

     amount_of_animals = 0

     def __init__(self, name):
          self.__name = name
          self.length = 0
          self.strength = 0

          Animal.amount_of_animals += 1

     def get_name(self):
          return self.__name

     def get_length(self):
          return self.length

     def set_length(self, length):
          self.length = length

     def get_strength(self):
          return self.strength

     def set_strength(self, strength):
          self.strength = strength

     # Eine Klassenfunktion:
     # Kann aufgerufen werden, ohne vorher ein Objekt gemacht zu haben
     # Erkennbar daran, dass self fehlt
     def compare_animals(animal1, animal2):
          pass


class Panda(Animal):
     
     def __init__(self):
          Animal.__init__(self, "Panda")
          self.cuteness = 9001

     def get_cuteness(self):
          return self.cuteness




objekt1 = Animal("Lilly")
objekt2 = Panda()
objekt2.set_strength(42)
Animal.compare_animals(objek1, objekt2)

print(Animal.amount_of_animals)


print(objekt1.get_name())
print(objekt2.get_name())


# Aufgabe 1
# Welche Attribute speichert die Klasse >Animal<?
# __name
# strength
# length


# Aufgabe 2
# Welche Klassenattribute speichert sie?
# amount_of_animals


# Aufgabe 2
# Welche Methoden stellt diese Klasse bereit?
# get_name
# get_length
# get_strength
# set_length
# set_strength


# Aufgabe 3
# Welche Klassenfunktionen stellt diese Klasse bereit?
# compare_animals


# Aufgabe 4
# Warum gibt es keinen Setter für das Attribut >name<?
# wir wollen name nicht nachträglich ändern. Warum sollten wir dann die Möglichkeit bieten?


# Aufgabe 5
# Welcher Zusammenhang besteht zwischen Panda und Animal?
# Panda ist eine Unterklasse von Animal.
# Damit ist Animal eine Überklasse von Panda
# Panda "erbt" alle Eigenschaften (Attribute und Methoden) von Animal
# Panda erweitert die bereits vorhandenen Eigenschaften um ein Attribute cuteness
# und um die Methode get_cuteness



