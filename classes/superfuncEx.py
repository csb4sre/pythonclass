
class Operations():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def values(self):
        return self.a, self.b

class Arthmatic(Operations):
    def __init__(self,a):
        self.b = b
        super(Operations,self).__init__(b)
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
op = Operations(2,3)

e1 = Arthmatic(5)
print(e1.add())
# print(e1.sub())
