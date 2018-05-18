for a in range(5):
    for i in range(a):
        print('*',end='')
    print('*')

a=1
b=1
print(id(a))
print(id(b))
a=2
print(id(a))