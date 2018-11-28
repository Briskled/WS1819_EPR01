user_input = int(input("Gib eine Zahl ein"))

# user_input % 2 == 0


# Wenn der input grade ist: output = "Die Zahl ist grade"
# Ansonsten: output = "Zahl ist ungrade"
#output = "Die Zahl ist gerade" if user_input % 2 == 0 else "Die Zahl ist ungerade"
#VARIABLE = WERT_1 if BEDINGUNG else WERT_2

#if user_input % 2 == 0:
#     output = "Die Zahl ist gerade"
#else:
#     output = "Die Zahl ist ungerade"



#user_input it 0 wenn er kleiner ist als 0. Ansonsten behalte ihn bei
user_input = 0 if user_input < 0 else user_input

#user_input it 9 wenn er größer ist als 9. Ansonsten behalte ihn bei
user_input = 9 if user_input > 9 else user_input


print(user_input)
