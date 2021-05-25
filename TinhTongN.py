def tinhtong(n):
    s=0
    for i in range(n+1):
        s= s+i
    print('tong cua day so la: %s'%(s))

n= int(input('moi nhap so luong ptu: '))
tinhtong(n)