a = 7
def bien():
    global a
    a = a*2
    print("Tich so la:",a)
if __name__ =="_main_":
    while True:
        bien()
        b = a+5
        print("Tong so laf",b)