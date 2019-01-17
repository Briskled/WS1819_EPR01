class Animal:
     def __init__(self, id, name):
          self.id = id
          self.name = name

class Panda(Animal):
     def __init__(self, coolness, id, name):
          super(Pandas, self).__init__(id, name)
          #Animal.__init__(self, id, name)
          self.coolness = coolness
          self.bamboo = None

     def hold(self, bamboo):
          self.bamboo = bamboo


class Bamboo:
     def __init__(self, height):
          self.height = height


b = Bamboo(6)
p = Panda(9000, 1, "Peter")
p.hold(b)
