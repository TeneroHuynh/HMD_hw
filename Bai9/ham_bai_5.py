def count_down(n):
    for i in range(n,0,-1):
        print(i)
    print('Start!!!')
    return

def tinh_S(n,x):
    S = 1
    for i in range(n):
        S *= x**2 + 1
    print('S = ',S)
    return
 
def tinh_A(n,x):
    a =1
    b =1
    for i in range(n):
        a *= x**2 + x + 1
    for i in range(n):
        b *= x**2 - x + 1
    print('A = ', a+b)
    return

def kt_snt(x):
    k = 0
    for i in range(2,x+1):
        if x % i == 0:
            k+= 1
    if k >1:
        print(f'{x} Không phải số nguyên tố')
    else:
        print(f'{x} Là số nguyên tố')
    return

