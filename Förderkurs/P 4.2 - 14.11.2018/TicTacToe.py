"""Docstring: Play TicTacToe
"""

__author__ = "1234567: Felix Lapp"
__credits__ = "Best tutorium ever <3"
__copyright__ = "by me"
__email__ = "felix.lapp@stud.uni-frankfurt.de"


def print_field():
     """Docstring: prints the current field seperated by |"""
     print(feld[0], feld[1], feld[2], sep="|")
     print("-"*5)
     print(feld[3], feld[4], feld[5], sep="|")
     print("-"*5)
     print(feld[6], feld[7], feld[8], sep="|")


name1 = None
name2 = None
punktzahl = 0
figur = None
runde = 0
feld = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

#    | |X
#   -----
#    | |O
#   -----
#   X|O|
#
#

current_player = None
current_symbol = None
symbol1 = None
symbol2 = None


# Ask both players for their names
name1 = input("Spieler 1, gib deinen Namen ein >>> ")
current_player = name1
name2 = input("Spieler 2, gib deinen Namen ein >>> ")

# TODO check if names are not too small or too large.

while True:
     name1_symbol = input(name1+", wähle dein Symbol aus (X oder O) >>> ")
     if name1_symbol == "X" or name1_symbol == "O":
          symbol1 = name1_symbol
          current_symbol = symbol1
          if name1_symbol == "X":
               symbol2 = "O"
          else:
               symbol2 = "X"
          break
     else:
          print("Deine Eingabe war falsch.")

          
# at this point the names of both players are known
# each player has chosen his symbol.

# Fragen, wo der spieler setzen will
# Funktion machen
#    gibt den Index innerhalb der Liste wieder
#    Der Spieler wird gefragt
#    Wiederholen bis er eine gültige Eingabe macht
def ask_for_placement():
     while True:
          user_input = input(current_player + ", An welche Stelle möchtest du setzen? >>> ")
          if user_input.isdigit():
               index = int(user_input)
               if index >= 0 and index <= 8:
                    return index
               else:
                    print("Bitte eine Zahl zwischen 0 und 8 eingeben")
          else:
               print("Bitte eine Zahl zwischen 0 und 8 eingeben")


def change_player(current_symbol, current_player):
     if current_symbol == "X":
          current_symbol = "O"
          current_player = name2
     else:
          current_symbol = "X"
          current_player = name1
     return current_symbol, current_player


while True:
     print_field()
     index = ask_for_placement()
     if feld[index] == " ":
          feld[index] = current_symbol
          current_symbol, current_player = change_player(current_symbol, current_player) #wechselt den spieler
     else:
          print("Feld ist schon belegt")






























