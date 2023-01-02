try :
    x=eval(input("nhap x: \n"))
    y=eval(input("nhap y: \n"))
    z=x/y
except NameError as errrrrr1:
    print("loi la loai :",errrrrr1)
except ZeroDivisionError as errrrrrr2:
    print("loai loi la: ",errrrrrr2)
else:
    print("x/y",z)