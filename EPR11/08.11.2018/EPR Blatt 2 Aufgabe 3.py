while True:
    print("In welcher Masseinheit ist die umzurechnende Temperatur?")
    unit = int(input("Anworten Sie: 1 für Kelvin, 2 für Celsius, 3 für\
 Fahrenheit: "))

    if(unit < 1 or unit > 3):   #if the given integer isnt 1, 2 or 3
                                #it will print an error.
        print("Die Eingabe war ungültig.")

    else:                       #we will differentiate between the
                                #possible units of the given temperature,
                                #determined by the variable "unit".
        temp = float(input("Wie viel Grad sind es in der angegebenden\
 Temperatur?: "))

    if(unit == 1):
        c = temp - 273.15
        f = temp*1.8 - 459.67
        print("Das sind", c, "° Celsius oder", f, "° Fahrenheit.")
        break
    elif(unit == 2):
        k = temp + 273.15
        f = temp*1.8 + 32
        print("Das sind", k, "° Kelvin oder", f, "° Fahrenheit.")
        break
    elif(unit == 3):
        k = (temp + 459.67) / 1.8
        c = (temp - 32) / 1.8
        print("Das sind", k, "° Kelvin oder", c, "° Celsius.")
        break

