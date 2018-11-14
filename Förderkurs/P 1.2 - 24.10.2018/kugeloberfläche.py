from math import pi

radius_string = input("Gib den Radius ein ")
radius = int(radius_string)                       # Convert input to a number
oberfl = 4*pi*radius*radius                       # Calculade Surface
print("Die Oberfläche ist", oberfl)
