def sole(n):
    t=0
    s=0
    for i in range(1,n+1):
        if i%2!=0:
           t=i*(-1)
        else:
            t=i 
        s=s+t
    print(s)
n=int(input("nhap so luong phan tu n: "))
sole(n) 