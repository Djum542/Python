from builtins import int

n = int(input("Nhap vao so phan tu can trong mang:"))
a = []
for i in range(0,n):
    print("Phan tu thu", i+1, "la:", end="")
    temp = int(input())
    a.append(temp)
    # for j in range(temp):
    if i % 2 !=0:
        print(temp)