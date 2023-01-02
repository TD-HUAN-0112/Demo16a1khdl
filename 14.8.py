x,y = 1,2
try:
    print("x/y ",x/y)        #lệnh x chia y tiềm ẩn khả năng xảy ra lỗi
except ZeroDivisionError as ex:
    print("error:",ex)
finally:                     #khối các lệnh ở dòng 7,8,9 luôn được thực thi
    print("x+y = " ,x+y)
    print("x-y = ", x-y)
    print("x*y = ",x*y)