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

    #print(options[inops])
    if inops == 1:
        print(options[inops])
        print(add(num1,num2))
        ops()
    elif inops == 2:
        print(options[inops])
        print(sub(num1,num2))
        ops()
    elif inops == 3:
        print(options[inops])
        print(mul(num1,num2))
        ops()
    elif inops == 4:
        print(options[inops])
        print(mod(num1, num2))
        ops()
    elif inops == 5:
        print(options[inops])
        print(mod(num1, num2))
        ops()
    elif inops == 6:
        print(options[inops])
        print(fldiv(num1,num2))
        ops()
    elif inops == 7:
        print(options[inops])
        print(expo(num1,num2))
        ops()


def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
def mod(x,y):
    return x%y
def fldiv(x,y):
    return x // y
def expo(x,y):
    return x**y

ops()
