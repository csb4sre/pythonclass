marks=int(input("Enter the marks: "))
if marks < 35:
    print("Student is failed")
elif marks > 34 and marks < 60:
    print("Student got 2nd class")
elif marks > 59 and marks < 101:
    print("Student got 1st class")
else:
    print("Wrong Marks entered.. Try again")
