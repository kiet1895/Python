# -*- coding: utf-8 -*-

from itertools import count


j=[]
for n in range(2000,3201):
      if (n%7==0) and (n%5!=0):
          j.append(str(n))
print(",".join(j))
tong=len(j)
txt="tong cac so chia het cho 7 la: %s"
print( txt %(tong))
