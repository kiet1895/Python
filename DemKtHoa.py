from curses.ascii import islower


s=input('moi ban nhap chuoi: ')
UpKey=0
LoKey=0
for i in str(s):
    if i.isupper():
        UpKey += 1
    if i.islower():
        LoKey+=1
print('Tong so kt in hoa la: ',UpKey)
print('Tong so kt thuong la: ',LoKey)
