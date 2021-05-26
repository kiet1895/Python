from calendar import c
from posixpath import split


# item=[ x for x in input("nhap chu can sap xep:").split(',')]
def r_file():
    f_in= open("mang.INP","r")
    line=f_in.readline().split(",")
    line.sort()
    # chuoi in hoa duoc sap xep truoc
    f_in.close()
    return(line)
def w_file(chuoi):
   f_out = open("mang.OUT","w") 
   f_out.write(chuoi)
   f_out.close()



# # a=[str(i) for i in line]
# # print(a[0])

chuoi = r_file()
# print(type(chuoi[1]))
a=''
for x in range(len(chuoi)):
    a= a +chuoi[x] +','
# print(a)
w_file(a) 