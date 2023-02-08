n = int(input("Nhap n: "))
list = []

for i in range(n):
    list.append(int(input()))
min = list[0]

for i in list:
    if i < min:
        min = i
print("Nho nhat trong list:",min)