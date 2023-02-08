a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
tong = 0
while a <= b:
    if a % 2:
        if a != 0:
            tong = tong + a
    a = a + 1
print("Tong cac so le tu a toi b la:  ", tong)
