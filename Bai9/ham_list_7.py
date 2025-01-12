
List_of_animals =['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']

def find_animal(List_of_animals,find):
    if find in List_of_animals:
        return f"There is {find} in list of animals"
    else:
        return f"{find} is not in list of animals"

def list_numbers():
    Lst = []
    S = 0
    list_greater_than_find = []
    Lst.append(int(input("Nhập giá trị")))
    a = int(input("Tiếp tục nhập giá trị? 1: Có, 0: Không"))
    while a == 1:
        nhap1 = int(input("Nhập giá trị: "))
        Lst.append(nhap1)
        a = int(input("Tiếp tục nhập giá trị? 1: Có, 0: 0"))
    find = int(input("Nhập giá trị cần tìm: "))
    print("List: ", Lst)
    for i in Lst:
        S += i
        if i > find:
            list_greater_than_find.append(i)
    print("Tổng các giá trị trong list: ", S)
    print(f"{find} xuất hiện {Lst.count(find)} lần trong list")
    if find > max(Lst):
        print(f"{find} lớn hơn tất cả các số trong list")
    else:
        print(f"{find} không lớn hơn tất cả các số trong list")
    print(F"Các số lớn hơn {find} trong list là: ", list_greater_than_find)

def list_number_2():
    Lst = []
    snt = []
    so_am = []
    so_duong = []
    Lst.append(int(input("Nhập giá trị")))
    a = int(input("Tiếp tục nhập giá trị? 1: Có, 0: Không"))
    while a == 1:
        nhap1 = int(input("Nhập giá trị: "))
        Lst.append(nhap1)
        a = int(input("Tiếp tục nhập giá trị? 1: Có, 0: 0"))
    print("List: ",Lst)
    for i in Lst:
        dem = 0
        if i > 0:
            so_duong.append(i)      
            if i>1:
                for k in range(2,i+1):
                    if i%k == 2:
                        dem += 1
                if dem < 2:
                    snt.append(i)
        elif i < 0:
            so_am.append(i)
    print("Các số nguyen tố trong list: ", snt)
    print("Các phần tử âm trong list: ", so_am)
    s=0
    dem1=0
    for u in so_am:
        dem1 += 1
        s+=u
    print("Trung bình cộng các phần tử ẩm: ",s/dem1)
    print("Các phần tử dương trong list: ",so_duong)
    s1 = 0
    dem2 = 0
    for u1 in so_duong:
        dem2 += 1
        s1 += u1
    print("Trung bình cộng các phần tử dương: ",s1/dem2)
    print("Giá trị max trong list", max(Lst))
    print("Giá trị min trong list", min(Lst))
    Lst.sort()
    print("List sắp tăng dần: ",Lst)




