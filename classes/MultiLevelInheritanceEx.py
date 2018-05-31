

class lion():
    def roar(self):
        print('lion is roaring')
    def hunt(self):
        print('Animal is hunting')

class tiger(lion):  #Level 1 sending lion as object to tiger
    def running(self):
        print('Animal is running')

class animal(tiger): #tiger class as object for animal class inherting lion class- Multi Level Inheritance
    def eating(self):
        print('The animal is eating')
    def sleep(self):
        print('The animal is sleeping')

a1 = animal()
a1.running()
a1.sleep()
