__author__ = "1234567: Felix Lapp"
__credits__ = ""
__email__ = "felix.lapp@stud.uni-frankfurt.de"



def ask_for_value(name):
     """Docstring: Asks User for a value
     Keeps asking until user inputs a valid value"""

     
     user_input = input("Welchen Wert hat " + name + "? >>> ")
     try:
          # returns the result if there is no error
          return float(user_input)
     except ValueError:
          print("Das war keine gültige Eingabe.")

          # otherwise ask again and return its value
          return ask_for_value(name)

     
def main():
     """Docstring: Main function"""

     # keys for dictionaries
     # write them im capslock because they should be constant
     KEY_NAME = "name"        
     KEY_HEIGHT = "größe"
     KEY_VALUE = "kampfwert"


     # Give every robot a name, a height and a value
     # using the keys we defined before
     
     #robo1 = {KEY_NAME: "Magnetron",
     #         KEY_HEIGHT: 3.5,
     #         KEY_VALUE: 9}
     #robo2 = {KEY_NAME: "Robostampf",
     #         KEY_HEIGHT: 6,
     #         KEY_VALUE: 17}
     #robo3 = {KEY_NAME: "Saboteur",
     #         KEY_HEIGHT: 0.5,
     #         KEY_VALUE: 11}
     #robo4 = {KEY_NAME: "Staubsauger 3000",
     #         KEY_HEIGHT: 0.3,
     #         KEY_VALUE: 1}


     # Give them no value because we want to set them later
     robo1 = {KEY_NAME: "Magnetron",
              KEY_HEIGHT: 3.5}
     robo2 = {KEY_NAME: "Robostampf",
              KEY_HEIGHT: 6}
     robo3 = {KEY_NAME: "Saboteur",
              KEY_HEIGHT: 0.5}
     robo4 = {KEY_NAME: "Staubsauger 3000",
              KEY_HEIGHT: 0.3}



     # Now set a value for every robot
     robo1[KEY_VALUE] = ask_for_value("Magnetron")
     robo2[KEY_VALUE] = ask_for_value("Robostampf")
     robo3[KEY_VALUE] = ask_for_value("Saboteur")
     robo4[KEY_VALUE] = ask_for_value("Staubsauger 3000")


     if robo1[KEY_VALUE] > robo3[KEY_VALUE]:
          print("MAGNETRON GEWINNT GEGEN SABOTEUR")
     else:
          print("SABOTEUR GEWINNT GEGEN MAGNETRON")



     if robo2[KEY_VALUE] > robo4[KEY_VALUE]:
          print("ROBOSTAMPF GEWINNT GEGEN STAUBSAUGER 3000")
     else:
          print("STAUBSAUGER 3000 GEWINNT GEGEN ROBOSTAMPF")


     # save every robot in a list so we can iterate through hem
     robos = [robo1, robo2, robo3, robo4]

     # the first saved robot can be everyone
     # if it is already the best one: nice!
     # if not: we will find it
     
     best_robo = robo1

     # iterate through all robots
     for r in robos:
          # if we found one with a higher value than the saved
          if r[KEY_VALUE] > best_robo[KEY_VALUE]:

               # save it!
               best_robo = r

     # at this point "best_robo" saves the robot with the highest value
     print("Der stärkste Roboter ist", best_robo[KEY_NAME], "mit dem Kampfwert", best_robo[KEY_VALUE])


if __name__ == "__main__":
     main()

