#print ist eine Funktion!!
# print("Hallo Welt")



def add(number1, number2):
     return number1 + number2


def is_even(number):
     """Docstring: Checks if the given number is even


     Ich mag Züge"""
     
     issesdenneven = number % 2 == 0
     return issesdenneven


n = int(input("Gib mir eine Zahl: "))
if is_even(n):
     print("Ist grade")
else:
     print("Ist nicht grade")




