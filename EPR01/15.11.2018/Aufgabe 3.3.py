#author

string = ""
# x counts the number of iterations
x = 1

#replace for with while :)
while x < 10:
     print("x is ", x)
     string += " " + str(x)
     print("Now, x is ", x)

     #add one to x so the loop wont be endless
     x += 1
print("All previous numbers: ", string)
