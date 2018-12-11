class Fahrzeug:
     """Class which is representing a vehicle"""
     
     def __init__(self):
          """Initializes the object"""
          print("Ich bin initialisiert")
          self.ps = 90
     
     def fahren(self):
          """drive"""
          print("Ich fahr jetzt")

     def kaputt_gehen(self):
          """boom"""
          print("Bin kaputt")





# Neues objekt der Klasse Fahrzeug
# Führt automatisch die __init__ Funktion aus
auto1 = Fahrzeug()
print("Auto1:", auto1.ps)
auto1.ps = 65
print("Auto1:", auto1.ps)

auto2 = Fahrzeug()
print("Auto2:", auto2.ps)












