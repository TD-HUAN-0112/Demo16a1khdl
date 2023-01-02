try:
    x = eval(input("nhap x\n"))
    y = eval(input("nhap y\n"))
    z=x/y
except (NameError, ZeroDivisionError) as errrrrrrr: # gop ca 2 loi
    print("loi kha nang la :",errrrrrrr)
else:
    print("x/y",z)