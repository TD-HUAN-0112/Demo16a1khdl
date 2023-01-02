#python program showing a scope of object 
def some_func():
    print("inside some_func()")
    def some_inner_func(): 
        var=10
        print("inside inner func() value of var", var)
    some_inner_func()           # goi ham some_func 
    #print("try printing var from outer function:  , var")
some_func