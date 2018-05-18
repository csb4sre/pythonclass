l = list(input("Enter few numbers"))

def pos(lst,n):
    for p in range(len(lst)):
        if p == n:
            print('n is in', p )

num = input("Enter a number from the list")
pos(l,num)
#print(l)
