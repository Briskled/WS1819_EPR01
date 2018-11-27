

players_list = [("Player1", "Melanie"), ["Karo Ass", "Kreuz Bube", "Kreuz Ass", "Karo 9"],\
                ("Player2", "Aylin"), ["Herz 7", "Pik 8"],\
                ("Player3", "Fahad"), ["Karo Dame", "Pik König", "Herz 9", "Herz König", "Herz 8"],
                ("Player4", "Anita"), []]
number_players = 4


while len(players_list) > 0:
     min_num = 32
     min_name = ""
     index = -1

     for i in range(number_players):
          #print("\n")
          index_name = 2*i
          index_cards = index_name + 1
          name_tuple = players_list[index_name]
          cards = players_list[index_cards]
          #print(name_tuple[1])
          #print(len(cards))
          if len(cards) < min_num:
               min_num = len(cards)
               min_name = name_tuple[1]
               index = index_name

     print(min_name, "hat", min_num, "Karten")
     players_list.pop(index)
     players_list.pop(index)
     number_players -= 1




def main():
     """Docstring"""
     #print("Ich bin die Main-Funktion von Ranking")
     pass


if __name__ == "__main__": #if this is the running program
     main()
