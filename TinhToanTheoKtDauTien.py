tientong =0
while True: 
    s= input("nhap lich su thu nhap: ")
    if not s:
        break
    value = s.split(" ")
    kt = value[0]
    tien= int(value[1])
    if (kt =="D"):
        tientong+=tien
    elif (kt=="W"):
        tientong-=tien
    else:
        pass
print("so tien con lai la:%s" %(tientong))
