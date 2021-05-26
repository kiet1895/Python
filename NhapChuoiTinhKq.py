import math
c=50
h=30
value=[]
item= [x for x in input('nhap gia tri:').split(',')]
print(item)
for d in item:
   value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(value))