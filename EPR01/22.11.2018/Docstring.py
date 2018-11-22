"""Docstring: Cooles Modul

Längere Beschreibung.....
.."""

__author__ = "1234567: Felix Lapp, 9876543: Peter Susi"
__author__ = "123456: John Cleese, 654321: Terry Gilliam"


import random





def hello_world():
     """Docstring: Kurze Beschreibung

     Ja printet so gedöns
     zweizeilig
     dreizeilig"""
     print("Hello World")     #printet

def repeat_input(message, min_value, max_value):
     """Requests an input from a user over and over again"""

     while True:
          user_input = input(message + " >>> ")
          print(user_input)
          if user_input.isdigit():
               number = int(user_input)
               print(number)
               if min_value <= number <= max_value:
                    return (number, user_input)
          print("Bitte eine Zahl zwischen "+str(min_value)+" und "\
                +str(max_value)+" eingeben")


#variable, user = repeat_input("Hallo gib ma was ein", -19362, 9)


def try_except():
     while True:
          user_input = input("Gib eine Zahl ein >>> ")
          try:
               number = int(user_input)
               print("Super, deine Zahl ist", number)
               break
          except ValueError:
               print("Das ist keine Zahl!")
          
          print("das passiert immer")


#try_except()

def is_number(string):
     """Docstring..."""
     try:
          int(string)
          return True
     except ValueError:
          return False

def main():
     print("Main")


if __name__ == "__main__":
     main()

random.seed()
print(random.randint(1, 10))
print(random.randint(5, 50))














