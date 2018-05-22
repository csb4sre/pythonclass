#__init__   is a special menthod used to initialise the class variables

class emp():
    def __init__(self, fname, lname, company, pay):
        self.fname = fname
        self.lname = lname
        self.company = company
        self.pay = pay
    def details(self):
        print('The name is {} {} and he belongs to {}'.format(self.fname,self.lname,self.company))
        print('the email id will be {}{}@gmail.com'.format(self.fname, self.lname))
        print('the sal for him is {}'.format(self.pay))
    def inc(self,val):
        print('the incremented sal of {} {} is {}'.format(self.fname, self.lname,self.pay+val))


emp1 = emp('Iron Man','Dude','avenger',50000)
emp1.details()
emp1.inc(5000)
