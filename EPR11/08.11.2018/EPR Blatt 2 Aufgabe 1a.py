secretNumber = 2
a = input("Geben Sie eine Zahl ein: ")
if(int(a) == secretNumber):
     print("Herzlichen Glückwunsch! Sie haben die Zahl erraten")
elif int(a) > 3 or int(a) < 1:
     print("Ungültige Eingabe")
else:
     print("Schade! Das war nicht die gesuchte Zahl.")


