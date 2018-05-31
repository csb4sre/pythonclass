import os

os.mkdir('imnew2')
os.chdir('imnew2')

a = open('metoo.txt','w')
a.write('I am newly created file')
a.close()

b = open('metoo.txt','r')
print(b.readline())
# 
# os.rmdir('..\\\imnew2')
