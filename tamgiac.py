def tamgiac(a,b,c):
    # print(a+b)
    if (a+b>c)and(a+c>b)and(b+c>a):
        return True
    return False
def dientich(a,b,c):
    dt=0
    if(a**2 == b**2 + c**2):
        dt == (1/2)*b*c
        print('dien tich hinh tam giac: %s'%dt)
    elif (b**2 == a**2 + c**2):
        dt = (1/2)*a*c
        print('dien tich hinh tam giac: %s'%dt)
    elif (c**2 == a**2 + b**2):
        dt = (1/2)*a*b
        print('dien tich hinh tam giac: %s'%dt)
    f_out.write(str(dt))
    f_out.close()

    
f_in= open("TAMGIAC.INP","r")
line=f_in.readline().split()
f_out = open("TAMGIAC.OUT","w")
a= [int(i) for i in line]

if tamgiac(a[0],a[1],a[2]):
    print('tao thanh tam giac')
    dientich(a[0],a[1],a[2])
else:
    print('khong tao thanh tam giac')
    f_out.write(str("-1"))
f_out.close()
f_in.close()
