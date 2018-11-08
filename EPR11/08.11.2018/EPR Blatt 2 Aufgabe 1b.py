import random

secret_number = random.randint(1, 100)
while True:
     a = input("Geben Sie eine Zahl ein: ")
     if(int(a) == secret_number):
          print("Herzlichen Glückwunsch! Sie haben die Zahl erraten")
          break
     elif int(a) > secret_number:
          print("Die gesuchte Zahl ist KLEINER")
     else:
          print("Die gesuchte Zahl ist GRÖSSER")


