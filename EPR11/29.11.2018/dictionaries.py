lst = ["Wert1", "Wert2", "Wert3"]
print(lst[0])
lst[2] = "Was anderes anderes"
print(lst)
lst.append("Wert4")

dictionary = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_small = "abcdefghijklmnopqrstuvwxyz"

#counter = 1
#for buchstabe in alphabet:
#     dictionary[buchstabe] = counter
#     counter += 1


#i = 0
#while i < len(alphabet):
#     big = alphabet[i]
#     small = alphabet_small[i]
#     dictionary[big] = small
#    i += 1


steckbrief = {}
steckbrief["Name"] = "Felix"
#steckbrief["Geschlecht"] = "m"
#steckbrief["Größe"] = 190
steckbrief["Handkarten"] = [("Karo", "Ass"), ("Herz", "Bube")]

steckbrief[5] = "Wert"

i = 5
i += 1


def func(i):
     i = 5
     return i



hallo = 6
print(id(hallo))
hallo = func(hallo)
print(id(hallo))


#immutables:
# int
# bool
# float
# str
# tuple
# frozenset





