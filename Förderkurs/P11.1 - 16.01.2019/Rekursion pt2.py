

def get_user_input():
     while True:
          var = input("Bitte geben Sie eine ganze Zahl zwischen 1 und 10 ein >>> ")
          if var.isdigit():
               number = int(var)
               if 1 <= number <= 10:
                    return number
               else:
                    print("Falsche Eingabe")
          else:
               print("Falsche Eingabe")


def get_user_input_rek():
     var = input("Bitte geben Sie eine ganze Zahl zwischen 1 und 10 ein >>> ")
     if not var.isdigit():
          print("Falsche Eingabe")
          return get_user_input_rek()

     number = int(var)
     if not 1 <= number <= 10:
          print("Falsche Eingabe")
          return get_user_input_rek()
     return number






user_input = get_user_input_rek()
