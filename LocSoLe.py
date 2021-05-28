import numbers
from re import I


value = input('moi nhap day so: ')
numbers = [x for x in value.split(',')]
a=[]
for s in range(len(numbers)):
    i= int(numbers[s])
    if (i%2==1):
         a.append(str(i))
print(','.join(a))