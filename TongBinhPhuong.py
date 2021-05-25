def binhphuong(n):
    s=0 
    sum=0 
    for i in range(n+1): 
        s= i**2
        sum=sum+s
        print('binh phuong cua so %i là: %s'%(i,s))
    print('tong binh phuong:%s'%(sum))
n= int(input('nhap so n: '))
binhphuong(n)