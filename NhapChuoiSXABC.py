from posixpath import split


item=[ x for x in input("nhap chu can sap xep:").split(',')]
item.sort()
print( ','.join(item))