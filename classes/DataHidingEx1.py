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


print(c1.a)  #public
print(c1._b)  #protected
# print(c1.__c)  #private

print(c1.infun1())
print(c1._infun2())
# print(c1.__infun3())

