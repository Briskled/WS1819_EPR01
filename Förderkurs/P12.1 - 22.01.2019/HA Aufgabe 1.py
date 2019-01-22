class Plant:
     def __init__(self):
          self.__height = 0
          self.is_blooming = True

     def grow(self):
          self.__height += 1

     def set_height(self, height):
          self.__height = height

     def get_height(self):
          return self.__height


class Flower(Plant):
     def __init__(self, color):
          Plant.__init__(self)
          self.__color = color

     def get_color(self):
          return self.__color

     def __add__(self, other):
          b = BunchOfFlowers(self)
          b.flower_list.append(other)
          return b
     

class Tree(Plant):
     def __init__(self):
          Plant.__init__(self)
          self.amount_of_leaves = 0

     def lose_leaves(self, lose):
          if self.amount_of_leaves >= lose:
               self.amount_of_leaves -= lose
          else:
               self.amount_of_leaves = 0

class BunchOfFlowers:
     def __init__(self, flower):
          if isinstance(flower, Flower):
               self.flower_list = [flower]
          else:
               raise ValueError("Gib mir ne Blume!")

     def make_present():
          print("Happy")

     def __str__(self):
          return "Ich bin ein Blumenstrauß mit " + \
                 str(len(self.flower_list)) + " Blumen."




f = Flower("red")
b = BunchOfFlowers(f)

     # Operator overloading
     # https://thepythonguru.com/python-operator-overloading/
