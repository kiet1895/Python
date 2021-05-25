def SoNguyenTo(n):
    if n<2:
        return False
    for i in range(2,n):
        if (n%i==0):
            return False
    return True

dem=0
i=2
sb=""
n= int(input('nhap n: ' ))
# while (dem<n):
while (i<n): 
    if(SoNguyenTo(i)):
        sb= sb + str(i)+" "
        # dem+=1
    i+=1
print(sb)
