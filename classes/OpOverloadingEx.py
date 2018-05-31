class exp():
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

	def __add__(self, other1):
		x = self.a+other1.a
		y = self.b+other1.b
		z = self.c+other1.c

		return exp(x,y,z)
	def __str__(self):
		return ('{}x^2+{}x+{}'.format(self.a,self.b,self.c))

expression1 = exp(1,2,3)
expression2 = exp(5,6,7)

print(expression1+expression2)




