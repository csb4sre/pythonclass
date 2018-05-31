class animal():
    def eating(self):
        print('The animal is eating')
    def sleep(self):
        print('The animal is sleeping')

class lion(animal):         #sending animal class as object for lion class
    def roar(self):
        print('lion is roaring')
    def hunt(self):
        print('Animal is hunting')

class tiger(animal):        #sending animal class as object for tiger class
    def running(self):
        print('Animal is running')

t1 = tiger()
t1.running()
t1.sleep()
