n = int(input("Nhap vao so phan tu cua mangr: "))
a = []
tong = 0
for i in range(n):
    # print("Gia tri cua phan tu thu",i+1,"la: ",end="")
    temp = int(input())
    a.append(temp)
    tong += i
    print(tong)
