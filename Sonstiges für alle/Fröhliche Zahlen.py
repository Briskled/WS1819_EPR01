"""Docstring: Reads a users input number and proofs if it is happy.

No idea if this is called "happy".
"""  

__author__ = "133724: Felix Lapp"
__copyright__ = "by me"
__email__ = "moodle"
__credits__ = "I thank my mom <3"


input_number = input("Gib eine Ganze Zahl ein: ")
if not input_number.isdigit():
     print("Lappen.")
else:

     #counts the number of iterations
     counter = 0
     while counter < 100:

          #the next number
          nbr = 0

          #input_number is a string. So this loop iterates over each "letter"
          for z in input_number:

               #z is a number in every case so we can cast it to int.
               znbr = int(z)

               #We add the squared number to nbr
               nbr += znbr ** 2

          if nbr == 1:
               print("Die Zahl ist fröhlich")
               break
          elif nbr == 4:
               print("Periodisch 4 erreicht. Nicht fröhlich")
               break

          # we need to set input_number to a string again so the for loop will work.
          input_number = str(nbr)
          counter += 1
