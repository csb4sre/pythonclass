# seek() ------> seek(ref, 0 or 1) -------> takes your cursor to ref position
# tell() ------> tell(ref, 0 or 1) -------> gives the position of the cursor

a = open('textsample.txt','r')

pos1 = a.read(24)
print(pos1)

tellpos1 = a.tell()
print(tellpos1)

seekpos1 = a.seek(11,0)
print(seekpos1)
