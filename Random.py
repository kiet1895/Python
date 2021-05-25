import random

while True:
    input('nhan enter: ')
    num = random.randint(1,6)
    print(' so %s'%num)
    op=input('chon de tiep tuc (y/n)')
    if(op=="n"):
        break
