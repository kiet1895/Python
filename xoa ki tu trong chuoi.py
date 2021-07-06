def xoa(n,m):
    s=n.find('s')
    for i in range(len(n)):
        str= n[i]
        while True:
            if str in m:
                chuoi= m.replace(str,'')
                m=chuoi
            else:
                break
    print(chuoi)

n= input('moi ki tu can loc bo: ')
m= input('moi nhap chuoi: ')
xoa(n,m)