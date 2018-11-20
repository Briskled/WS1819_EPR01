# Aufgabenteil a)

continents = ["Afrika", "Europa", "Südamerika", "Nordamerika",\
              "Asien", "Antarktis", "Australien"]

for c in continents:
     print(c)




# Aufgabenteil b)
print("\n"*4)

for c in continents:
     if c == "Antarktis":
          continue
     print(c)




# Aufgabenteil c)
print("\n"*4)

anything = [1,5,2,6, "Peter", "Hugo", "Susi", "Europa", "Asien"]
for a in anything:
     if a in continents:
          print(a)




# Aufgabenteil d)
print("\n"*4)

amount = 0
for a in anything:
     if a in continents:
          amount += 1
print("In anything sind", amount, "Kontinente.")



#Aufgabenteil e)
print(len(continents))











