while True:
     user_input = input("Gib eine ganze Zahl ein >>> ")
     try:
          #Das hier versuch ich
          number = int(user_input)
          print("Zahl eingegeben:", number)
     except ValueError:
          print("Falsche Eingabe")
