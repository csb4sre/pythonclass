def fun1():
    '''This is a sample function and this is doc string'''
    print('Hello I am from fun1')
fun1()
print(fun1.__doc__) #prints the document related to the function
print(fun1) #prints the function name space
print(id(fun1)) #prints the address of the function
print(type(fun1)) # prints the type as function

# IMP - One should define/pass the parameters in functions by order.
# First the positional and then default values

# Variable length argument

# Type -1
def greetings(*names):
    for name in names:
        print ('Welcome', name, 'to python class')

greetings('student1', 'student2','students3' )

#Type -2
def info (**details):
    for hero,location in details.items():
        print(hero, ' is from ', location)

info (ironman = 'usa', thor = 'sky', blackpanther = 'wakanda')

# LAMBDA function
# Its an anonymous function written in a single line without keyword 'def'
squ = lambda a:a**2
print(squ(5))

# map() will give you True or False
# filter() filters the sequence on your condition

l = [a for a in range(1,21)]
print(l)

odd = list(map(lambda a:a%2 != 0,l))
print(odd)
print(50*'-')

evn = list(map(lambda a:a%2 == 0,l))
print(evn)
print(50*'-')

evn = list(filter(lambda a:a%2 == 0,l))
print(evn)

# To get square root
print(9**(1/2))
