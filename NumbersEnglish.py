iNum = input("Enter a Number:")
lNum = len(iNum)
print(lNum)
iMatch = {3:'Hundred',
          4:'Thousand',
          6:'Lakh',
          8:'Crore'}

print(iMatch[lNum])
print()