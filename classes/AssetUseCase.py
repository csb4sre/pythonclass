#                                     Digital Lync
#                                 1st floor   2nd floor
#                             1R1 1R2 1R3     2R1 2R2 2R3
#                         tab,chair           tab,chair
#
# Table - type1, type2
# chair - type1, type2
# tv - big, small
# put above in csv file
#
# Every Asset has name, location and price

class detailsIn():
    """docstring for detailsIn. Takes input and saves in csv"""
    # def __init__(self, arg):
    #     super(detai Takes input and saves in csvlsIn, self).__init__()
    #     self.arg = arg
    #      Takes input and saves in csv
    def __init__(self, company, floor, room, invitem, invtype):
        self.company = company
        self.floor = floor
        self.room = room
        self.invitem = invitem
        self.invtype = invtype
    def printdetails(self):
        print('The {} is located on {}st floor, room-{}'.format(self.invitem,self.floor,self.room))

detin = detailsIn('DL','1','2','table','2')
detin.printdetails()
