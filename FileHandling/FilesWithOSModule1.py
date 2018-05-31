import os

print(os.getcwd())
os.mkdir('dummy3')
print(os.getcwd())
# os.chdir('dummy3')
# print(os.getcwd())
# # os.chdir('..\dummy1')
# print(os.getcwd())
# os.chdir('c:\\users\\cballa')
# print(os.getcwd())

os.rmdir('dummy3')
os.rename('dummy1','dummy')
