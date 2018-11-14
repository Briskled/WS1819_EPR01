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
feld = [" ", " ", "X", " ", " ", "O", "X", "O", " "]

#    | |X
#   -----
#    | |O
#   -----
#   X|O|
#
#

current_player = None
symbol1 = None
symbol2 = None


# Ask both players for their names
name1 = input("Spieler 1, gib deinen Namen ein >>> ")
name2 = input("Spieler 2, gib deinen Namen ein >>> ")

# TODO check if names are not too small or too large.

while True:
     name1_symbol = input(name1+", wähle dein Symbol aus (X oder O) >>> ")
     if name1_symbol == "X" or name1_symbol == "O":
          symbol1 = name1_symbol
          if name1_symbol == "X":
               symbol2 = "O"
          else:
               symbol2 = "X"
          break
     else:
          print("Deine Eingabe war falsch.")

          
# at this point the names of both players are known
# each player has chosen his symbol.












