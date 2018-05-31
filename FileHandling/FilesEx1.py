
a = open('sample1.txt','w')
a.write('this is my first line in file example')
a.close()

b = open('sample1.txt','w')
b.write('this is my second line in file example')
b.close()

c = open('sample1.txt','a')
c.write('this is my third line in file example')
c.close()
