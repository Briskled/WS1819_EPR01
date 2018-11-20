


while True:
     i = input("Geben Sie eine ganze Zahl ein >>> ")

     # try führt etwas aus und bricht ab, sobald es zu einem Fehler kommt
     try:
          zahl = int(i)  # hier kann ein ValueError auftreten. Sollte das passieren
                         # werden die nächsten beiden Zeilen nicht mehr ausgeführt
          print("Passt")
          break

     # wenn im try-block ein ValueError auftritt wird dieser abgebrochen und stattdessen
     # der except-block ausgeführt
     # Sollte ein anderer Error als ein ValueError auftreten
     # gibt es wie gewohnt eine Fehlermeldung
     except ValueError:
          print("Error")
          


#Statt except ValueError: könnt ihr auch nur except schreiben
#except:  Das würde jeden Error abfangen. BENUTZT DAS NICHT!
#         Es kann vorkommen, dass ein anderer Fehler auftaucht als ihr erwartet.
#         Dann sucht ihr lange an einer falschen stelle
