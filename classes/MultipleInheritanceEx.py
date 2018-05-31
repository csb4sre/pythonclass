

class lion():         
    def roar(self):
        print('lion is roaring')
    def hunt(self):
        print('Animal is hunting')

class tiger():
    def running(self):
        print('Animal is running')

class animal(tiger,lion): #both tiger and lion classes as objects for animal class - Multiple Inheritance
    def eating(self):
        print('The animal is eating')
    def sleep(self):
        print('The animal is sleeping')

a1 = animal()
a1.running()
a1.sleep()
