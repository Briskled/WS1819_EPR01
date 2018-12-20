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

     def __init__(self):
          self.cards = []
          sbls = ["Karo", "Pik", "Kreuz", "Herz"]
          vals = ["Ass", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König"]
          for s in sbls:
               for v in vals:
                    self.cards.append(Card(s, v))

     def shuffle(self):
          random.shuffle(cards)

     def pop_card(self):
          return shuffle.pop()

     def add_card(self, card):
          cards.append(card)

class Game:

     def __init__(self, deck, players):
          self.players = players
          self.deck = deck
          self.openstack = [deck.pop_card()]
          self.current_player_index = 0

     def get_current_player(self):
          return self.players[0]

     def next_player(self):
          self.current_player += 1
          self.current_player %= self.amount_of_players()

     def amount_of_players(self):
          return len(self.players)

     def get_opened_card(self):
          return openstack[0]

class Player:

     def __init__(self, name):
          self.name = name
          self.cards = []

     def pop_card(self, index):
          return self.cards.pop(index)

     def __str__(self):
          return "Player: "+self.name


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
     deck = Deck()

     game = Game(deck, players)

if __name__ == "__main__":
     main()
