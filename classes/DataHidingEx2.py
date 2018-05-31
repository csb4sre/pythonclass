class c1():
	a = 1
	_b = 2
	__c = 5
	def infun1():
		b = 6
		return b
	def _infun2():
		ad = 9
		return ad
	def __infun3():
		add = 6443
		return add

# class c2(c1):
# 	def infun4():
# 		print(c1.a)
# 		print(c1._b)
# 		print(c1.__c)

# print(c1.a)  #public
# print(c1._b)  #protected
# # print(c1.__c)  #private

# print(c1.infun1())
# print(c1._infun2())
# # print(c1.__infun3())

obj = c1()
print(obj.a)
print(obj._b)
print(obj._c1__c) #Private variables/functions can be accesed by calling the class as protected. 

# callc1 = c1()
# callc2 = c2(callc1)
# callc2.infun4()


