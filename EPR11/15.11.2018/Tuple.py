"""Docstring: Calculates all combinations of classes
"""

__author__ = "1234567: Felix Lapp"
__credits__ = "Coole credits"
__email__ = "felix.lapp@stud.uni-frankfurt.de"

letters = ["a", "b", "c", "d", "e"]
classes = [1,2,3,4,5,6,7,8,9,10,11,12]

liste = []
for i in letters:
     for y in classes:
          t = (y, i)
          liste.append(t)

def main():
     """Docstring: Main Funktion"""
     print("Sind main")

if __name__ == "__main__":
     main()


list_of_names = ["Engin", "Mimoun", "Ilia"]
list_of_cards = [[("Pik", "8"), ("Pik", "9")], ("Kreuz", "Bube"), ("Herz", "Dame")]
list_of_points = [0, 0, 0]
number_of_players = len(list_of_names)
current_player = 1

while True:
     name = list_of_names[current_player]
     card = list_of_cards[current_player]
     list_of_points[current_player] = 1
     # hier passiert so das spielgedöns
     print(name)
     print(card)

     current_player += 1
     if current_player >= number_of_players:
          current_player = 0


















