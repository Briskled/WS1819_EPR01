class Wheel:

     def __init__(self, vehicle):
          self.radius = 0
          self.vehicle = vehicle

     def turn(self):
          print("Rad dreht sich")


class Vehicle:

     def __init__(self):
          self._label = ""
          self.__speed = 0
          self.__color = ""
          self.__wheels = [Wheel(self)]


     def get_label(self):
          return self._label

     def get_speed(self):
          return self.__speed

     def set_speed(self, speed):
          self.__speed = speed

     def get_color(self):
          return self.__color

     def set_color(self, color):
          self.__color = color

     def get_wheels(self):
          return self.__wheels

     def add_wheel(self, wheel):
          if len(self.__wheels) <= 3:
               self.__wheels.append(wheel)

     def drive(self):
          for w in self.__wheels:
               w.turn()

class Car(Vehicle):

     def __init__(self):
          Vehicle.__init__(self)
          self.ps = 0

     def get_ps(self):
          return self.ps

     def set_ps(self, ps):
          self.ps = ps



v = Vehicle()

