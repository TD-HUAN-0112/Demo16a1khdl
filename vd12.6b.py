# var11 is in the global namespace
var = 5
def sum_func():
    #var2 is in the local namespace 
    var= 6
    print("gia tri bien var trong local name ham some_func la:",var)
    def some_inner_func():

        #var3 = 7
        var=7
        print("gia tri bien var trong nested local namespace la:", var)
    some_inner_func()
print("gia tri bien var trong khong gian local namespace la:",var)

sum_func()
print("gia tri bien var trong local name ham some_func la:",var)