# ví dụ về sử dụng assert
def tinhTB(hk1,hk2):
    assert(hk1 >+0 and hk2>=0), 'ca diem hk1 va hk2 phai >=0'
    TB=(hk1+hk2*2)
    return TB
print(tinhTB(8,7.5))
print(tinhTB(1,6))