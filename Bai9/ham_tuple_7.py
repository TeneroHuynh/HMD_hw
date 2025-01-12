def tuple_string_1():
    Tpl = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')
    num1 = int(input("Nhập số từ 0 đến 9: "))
    num2 = int(input("Nhập số từ -1 đến -9: "))
    find = input("Nhập chuỗi cần tìm: ")
    print("Tuple: ",Tpl)
    print(f"Tuple[ {num1} ] =", Tpl[num1])
    print(f"Tuple[ {num2} ] =", Tpl[num2])
    print(f"{find} xuất hiện trong tuple {Tpl.count(find)} lần")


def tuple_number():
    tup_a = (3,1,2,4)
    tup_b = (5,7,6,8)
    tup_c = tup_a + tup_b
    tup_d = sorted(tup_c)
    print("Tuple a: ",tup_a)
    print("Tuple b: ",tup_b)
    print("Tuple c: ",tup_c)
    print("Tuple d: ",tup_d)
    print("Tuple[3]= ",tup_d[3])
    print("3 phần tử cuối cùng của tuple d",tup_d[-3:])