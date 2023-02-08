n = int(input("Nhap n: "))

list = []

for i in range(n):
    list.append(int(input()))

tong = 0
for j in list:
    tong = tong + j
print("Tong cac phan tu trong list: ",tong)