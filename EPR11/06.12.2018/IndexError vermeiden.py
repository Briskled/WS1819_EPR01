liste1 = [1,2,3,4]
liste2 = [4,5,6,7]
liste3 = [7,8,9,0]

liste = [liste1, liste2, liste3]



def get_stone(field, x, y):
     if 0 <= x <= 8 and 0 <= y <= 9:
          return field[x][y]
     else:
          return None



index = int(input("Gib eine Spaltennummer an >>> "))
