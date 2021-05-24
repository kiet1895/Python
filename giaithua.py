def giaithua(n):
    if n== 1:
     return 1
    else: 
         return n* giaithua(n-1)
if __name__ == '__main__':
    n= int(input("nhap n :"))
    print("ket qua "+ str( giaithua(n)))
    
