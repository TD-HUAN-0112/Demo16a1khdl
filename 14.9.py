try:
    a= int(input("nhập một số nguyên dương nhỏ hơn 100: "))
    #sinh ra lỗi khi số quá bé
    if a<=0:
        raise ValueError("bạn đã nhập 1 số quá nhỏ")
    #sinh ra lỗi quá lớn
    if a>100:
        raise ValueError("bạn cần nhập số nhỏ hơn 100!")
    #bắt lỗi
    #- nhập số không phải là số nguyên
    #- nhập số quá lớn (>100)
    #- nhập số quá bé 
except ValueError as errr:
    print(errr)