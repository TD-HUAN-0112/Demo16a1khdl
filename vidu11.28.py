# Nhập ma trận
a=[]
m=int(input('nhập số tự nhiên m:'))
n=int(input('nhập số tự nhiên n:'))
for i in range(m):
    print('chuẩn bị nhập chỉ số ma trận hàng thứ',i+1,':')
    b=[]
    for j in range (n):
        x=int(input('nhập phần tử thứ '+ str(j+1)+':'))
        b=b+[x]
    a.append(b)
    print('ma trận A đã nhập xong !')
    # in ma trận A ra màn hình
for i in range(m):
    for j in range(n):
        print(a[i][j],end='')
        print()
        #kiểm tra bằng cách in list A ra màn hình
        print(a)