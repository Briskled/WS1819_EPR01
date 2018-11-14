n = int(input("Gib die Zahl n ein: "))

# Startpunkt wo unsere Schleife beginnt
i = 1

# Startwert der Summe
summe = 0

# Schleife wird wiederholt solange i <= n
while i <= n:

     # 2*i-1 errechnet die i-te ungerade Zahl. Sie wird auf die Summe addiert
     summe += 2*i-1

     # i wird in jedem Durchlauf erhöht
     i += 1

#Summe ausgeben 
print("Die Summe ist", summe)





# Wie addieren wir überhaupt die ungeraden Zahlen
# Wo speichern wir das Ergebnis? in einer Variable     Yay
# Woher weiß die Schleife, wann sie aufhören soll?     Yay
# Woher weiß ich die i-te ungerade Zahl?    2i-1       Yay
# Wie wird die Summe ausgegeben?                       Yay                 


# 1 + 3 + 5 + 7 + ... + 2n-1
