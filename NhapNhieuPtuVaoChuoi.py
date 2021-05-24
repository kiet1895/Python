from pickle import APPEND


n= input('moi nhap n: ')
a=[]
for i in range(n):
    a.append(input('Moi nhap ptu thu %s: ' % (i+1)))
print(a)