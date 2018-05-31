

class lion():
    def roar(self):
        print('lion is roaring')
    def hunt(self):
        print('Lion is hunting')

class tiger(lion):
    def running(self):
        print('tiger is running')
    def hunt(self): #same method as in lion class
        print('tiger is hunting')

# class animal(tiger): #tiger class as object for animal class inherting lion class- Multi Level Inheritance
#     def eating(self):
#         print('The animal is eating')
#     def sleep(self):
#         print('The animal is sleeping')

# a1 = animal()
# a1.running()
# a1.sleep()

obj = lion()
obj.hunt()
