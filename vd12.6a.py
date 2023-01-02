# var11 is in the global namespace
var1 = 5
def sum_func():
    #var2 is in the local namespace 
    var2 = 6
    print("gia tri bien var2 trong local name ham some_func la:",var2)
    def some_inner_func():

        #var3 = 7
        var3=7
        print("gia tri bien var trong nested local namespace la:", var3)
    some_inner_func()
print("gia tri bien var trong khong gian local namespace la:",var1)

sum_func() 