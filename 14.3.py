while True: 
    try:
        x=int(input("nhap so x:"))
        break
    except ValueError:
        print("bi loi, hay nhap lai ngay!!")
print("X=",x)