import calc
from calc import *

def ops():
    options = ('0. Exit','1. Addition','2. Subtraction','3. Multiply','4. Division','5. Modulus','6. Floor Division','7. Exponent')
    print(options)
    inops = int(input("Please enter the operation from the list: "))
    if inops == 0:
        print("THANK YOU FOR USING MY CALC PROGRAM")
        exit()
    elif inops > 7:
        print("Enter correct value or 0 to exit")
        ops()
    else:
        pass
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if inops == 1:
        print(options[inops])
        print(add.add(num1,num2))
        ops()
    elif inops == 2:
        print(options[inops])
        print(sub.sub(num1,num2))
        ops()
    elif inops == 3:
        print(options[inops])
        print(mul.mul(num1,num2))
        ops()
    elif inops == 4:
        print(options[inops])
        print(div.div(num1, num2))
        ops()
    elif inops == 5:
        print(options[inops])
        print(mod.mod(num1, num2))
        ops()
    elif inops == 6:
        print(options[inops])
        print(fldiv.fldiv(num1,num2))
        ops()
    elif inops == 7:
        print(options[inops])
        print(expo.expo(num1,num2))

ops()
