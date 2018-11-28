def how_about_numbers(number):
     number += 16
     print("In der Funktion ist number =", number)

def how_about_strings(string):
     string = string.replace("l", "b")
     print("In der Funktion ist string =", string)

def how_about_lists(lst):
     lst[1] = 4
     print("In der Funktion ist list =", lst)

def how_about_dicts(dictionary):
     dictionary["Test"] = "Test"
     print("In der Funktion ist dictionary =", dictionary)


number = 7
how_about_numbers(number)
print("Außerhalb der Funktion ist number =", number)


string = "Hallo Welt"
how_about_strings(string)
print("Außerhalb der Funktion ist string =", string)


lst = [4,5,6]
how_about_lists(lst)
print("Außerhalb der Funktion ist lst =", lst)


dictionary = {"Anfang" : "Ein Element"}
how_about_dicts(dictionary)
print("Außerhalb der Funktion ist dictionary =", dictionary)
