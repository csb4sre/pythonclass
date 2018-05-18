iNum = int(input("Enter a Number: "))
#iNum = int(Num)

if iNum < 0:
    print("It is a Negative Number")
    if iNum > 0:
        print("It is a Positive Number")
else:
    print("It is a ZERO")

if iNum % 2 == 0:
    print(" and even")
else:
    print(" and odd")

