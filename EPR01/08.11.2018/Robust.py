# Hier wird gezeigt, wie man ein Programm robust schreiben kann
# Es soll bei jeder noch so falschen Eingabe nicht mit einer Fehlermeldung enden.

# Benutzer gibt etwas ein. user_input ist ein string!
user_input = input("Gib eine Zahl ein >>> ")

# jeder String stellt die Funktion isdigit() bereit. Sie nimmt die Werte
# False oder True an, je nachdem ob es sich beim String um eine (ganze) Zahl handelt oder nicht.
if user_input.isdigit():
     number = int(user_input)
     print("Klappt:", number)
else:
     print("Hast Schwachsinn eingegeben.")






banale = "6.5"

# Im try-block kann "versucht" werden, etwas zu tun...
try:
     f = float(banale)
     print("Klappt:", f)
# sollte dabei ein ValueError auftreten wird anstatt den
# Fehler auszugeben, der exept-block ausgeführt
except ValueError:
     print("Klappt nich")
