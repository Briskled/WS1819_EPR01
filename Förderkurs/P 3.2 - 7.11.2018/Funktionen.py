


def addiere(an, bo):
     """
     Docstring: Addiert an und bo und gibt das Ergebnis zurück
     """

     return an + bo




def find_minimum(liste):
     """
     Docstring: Findet das Minimum der gegebenen Liste und gibt es zurück
     """
     minimum = liste[0]
     for element in liste:
          if element < minimum:
               minimum = element
     return minimum



# Die funktionen können erst aufgerufen werden NACHDEM sie definiert wurden
print(addiere(42, 1337))
print(find_minimum([1]))
