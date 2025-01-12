import math
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
def tinhGTBT(x,y):
    try:
        mau = 2*x + 7*y
        tu = 5*x - y
        A = math.sqrt(tu/mau)
        if x == 0:
            raise ValueError("x phải khác 0")
        else:
            print('A = ',A)
    except ValueError as e:
        print('Error:',e)
        A = None
tinhGTBT(x,y)
