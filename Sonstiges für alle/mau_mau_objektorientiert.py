"""UNFERTIG!!"""

import random

class Card:
     def __init__(self, symbol, value):
          self.__symbol = symbol
          self.__value = value

     def get_symbol(self):
          return self.__symbol

     def get_value(self):
          return self.__value

     def can_lay_on(self, other_card):
          return self.__value == other_card.__value or \
                 self.__symbol == other_vard.__symbol


class Deck:

     def __init__(self, cards):
          self.cards = cards

     def shuffle(self):
          random.shuffle(cards)

     def pop_card(self):
          return shuffle.pop()

     def add_card(self, card):
          cards.append(card)

class Player:

     def __init__(self, name):
          self.name = name
          self.cards = []

     def pop_card(self, index):
          return self.cards.pop(index)


def get_number_of_players():
     user_input = input("Wie viele Spielen mit? >>> ")
     if not user_input.isdigit():
          print("Bitte Zahl zwischen 2 und 4 eingeben")
          return get_number_of_players()
     number = int(user_input)
     if 2 <= number <= 4:
          return number
     print("Bitte Zahl zwischen 2 und 4 eingeben")
     return get_number_of_players()

def get_players(number_of_players):
     remaining = number_of_players
     players = []
     while remaining > 0:
          user_input = input("Wie soll Spieler " + str(number_of_players - remaining + 1) + " heißen? >>> ")
          if user_input == "":
               name = "Spieler "+str(number_of_players - remaining + 1)
          else:
               name = user_input
          players.append(Player(name))
          remaining -= 1
     return players
     
def main():
     number_of_players = get_number_of_players()
     players = get_players(number_of_players)

if __name__ == "__main__":
     main()
