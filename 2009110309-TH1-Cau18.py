a = int(input("Nhap vao so a:"))
b = int(input("Nhap vao so b:"))
c = int(input("Nhap vao so c:"))
if a<b<c:
    print(c)
elif c<b<a:
    print(c)
elif c<a<b:
    print(b)