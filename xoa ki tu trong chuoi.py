def xoa(n,m):
    s=n.find('s')
    for i in range(len(n)):
        str= n[i]
        for x in range(len(m)):
            if str==m[x]:
                # print(m)
                chuoi = m.replace(str,'')
        m=chuoi
    print(chuoi)

n= input('moi nhap chuoi ma hoa: ')
m= input('moi nhap chuoi can loc bo: ')
xoa(n,m)