class Player:
     """Docstring: Represents a player playing maumau"""


     # Dies ist der Konstruktor
     def __init__(self, name):
          """Initializes the object"""

          # Ein Objekt der Klasse Player speichert zwei Attribute:
          # Ein Attribut ist cards
          self.cards = []

          # Das andere ist name
          self.name = name


class Card:
     """Docstring: Represents a card"""
     
     def __init__(self, color, value):
          """Initializes the card"""
          self.color = color
          self.value = value

     def can_be_together(self, card):
          """checks if this card can be layed together with another card"""
          
          if self.color == card.color or self.value == card.value:
               return True
          else:
               return False



if c1.can_be_together(c2):
     pass #then lay card down...


# Es werden 4 Objekte der Klasse Player erstellt
# Der String in den Klammern kommt oben im
# Konstruktor als Variable >name< an
player1 = Player("Anita")
player2 = Player("Beyda")
player3 = Player("Fahad")
player4 = Player("Quan")

o# Ich erstelle zwei objekte der Klasse Card
c1 = Card("Pik", "Bube")
c2 = Card("Karo", "Bube")

# Die Karte c1 füge ich der cards-liste im player1-objekt hinzu
player1.cards.append(c1)


print(player1.cards)
print(player2.cards)
print(player3.cards)
print(player4.cards)
