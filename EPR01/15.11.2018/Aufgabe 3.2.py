# author
import random

counter = 0
random_number = 0
while random_number != 18:
     counter += 1
     random_number = random.randint(10, 99)
print("Es hat", counter, "Versuche gebracht")








counter = 0
random_number = 0
while True:
     counter += 1
     random_number = random.randint(10, 99)
     if random_number == 18:
          break
print("Es hat", counter, "Versuche gebracht")
