# def disp(a):
# 	return 'This is parent {}'.format(a)
# def deco(fun):
# 	def fun_w(fun):
# 		return 'This is the actual name {}'.format(fun(a))
# 	return fun_w
# print (disp('super'))


# def disp(a):
# 	return 'This is parent {}'.format(a)
# def deco(fun):
# 	def fun_w(fun):
# 		return 'This is the actual name {}'.format(fun)
# 	return fun_w

# funcname = deco(disp)
# print(funcname)
# print (disp('super'))
# print(funcname('I am parent'))


def fun_deco(fun):
	def fun_wrap(a):
		return '{}'.format(a)
	return fun_wrap

@fun_deco
def disp(a):
	return 'The parent name is {}'.format(a)

print(disp('Khan'))
