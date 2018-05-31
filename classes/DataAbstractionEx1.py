class voting():
	__minvote = 0
	__name = ""

	def __init__(self):
		self.__minvote = 200
		self.__name = 'KCR'

	def results(self,addvote):
		print('The vote count is {} '.format(addvote+self.__minvote))

	
family1 = voting()
family1.results(5)

print(family1._voting__minvote)


