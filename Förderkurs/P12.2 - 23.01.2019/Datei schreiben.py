lst = ["Hallo", 7, "Tutorium", "EPR ist cool"]

file = open("testfile.txt", "x")
file.write(str(lst))
file.close()
