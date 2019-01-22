#Aufgabe 3 a)

def rek_1(n):
     if n == 0:
          return 1
     return 2 * rek_1(n-1)

def rek_2(n):
     if n == 0:
          return 0
     return 3 * rek_2(n//2) + 2


def iter_1(n):
     erg = 1
     for i in range(n):
          erg *= 2
     return erg


# MIT EINER FOR-SCHLEIFE:
# 1. Wie oft läuft die Rekursion durch?
#    n mal -> Schleife mit n Durchläufen
# 2. Eine Variable einführen
# 3. Rekursionsanfang in die Variable schreiben
#    Wenn Rekursionsanfang 0 ist -> Variable = 0
# 4. Was passiert denn überhaupt in der Rekursion?
#    Das vorherige Ergebnis wird mit 2 multipliziert
#    Also multiplizieren wir in unserer Schleife
#    die Variable mit 2
