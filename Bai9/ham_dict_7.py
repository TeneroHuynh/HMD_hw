def dict_danh_ba():
    danh_ba = {"Johnny": "0989741258","Katherine": "0903852147","Misu": "0913753951" ,"Jack": "0933753654"}
    a= int(input("Bạn muốn làm gì: "))
    if a == 1:
        print("Danh bạ điện thoại: ",danh_ba)
    if a == 2:
        ten = input("Nhập tên cần tìm: ")
        print(f"{ten} có số điện thoại là: ",danh_ba[ten])
    if a == 3:
        new_name = input("Nhập tên: ")
        new_phone = input("Nhập sđt: ")
        danh_ba[new_name] = new_phone
        print("Danh bạ điện thoại:", danh_ba)
    b = int(input("Tiếp tục lựa chọn? 1: Có, 0: Không"))
    while b == 1:
        a= int(input("Bạn muốn làm gì: "))
        if a == 1:
            print("Danh bạ điện thoại: ",danh_ba)
        if a == 2:
            ten = input("Nhập tên cần tìm: ")
            print(f"{ten} có số điện thoại là: ",danh_ba[ten])
        if a == 3:
            new_name = input("Nhập tên: ")
            new_phone = input("Nhập sđt: ")
            danh_ba[new_name] = new_phone
            print("Danh bạ điện thoại:", danh_ba)
        b = int(input("Tiếp tục lựa chọn? 1: Có, 0: Không"))   

def dict_tu_dien():
    tu_dien = {"cat": "con mèo","dog":"con chó","ant":"con kiến","bear":"con gấu"}
    a= int(input("Bạn muốn làm gì: "))
    if a == 1:
        print("Xem từ điển ",tu_dien)
    if a == 2:
        tu = input("Nhập từ cần tra: ")
        if tu in tu_dien:
            print(f"{tu} có nghĩa là: ",tu_dien[tu])
        else:
            print("Không tìm thấy trong từ điển")
    if a == 3:
        new_word = input("Nhập từ tiếng Anh: ")
        new_mean = input("Nhập nghĩa Việt: ")
        tu_dien[new_word] = new_mean
        print("Dictionary:", tu_dien)
    if a == 4:
        del_word = input("Nhập từ cần xóa: ")
        ask = int(input("Bạn có thật sự muốn xóa hay không? 1: Xóa, 0: Không"))
        if ask == 1:
            del tu_dien[del_word]
            print("Đã xóa từ trong từ điển")
            print("Dictionary: ",tu_dien)
    b = int(input("Tiếp tục lựa chọn? 1: Có, 0: Không"))
    while b == 1:
        a= int(input("Bạn muốn làm gì: "))  
        if a == 1:
            print("Xem từ điển ",tu_dien)
        if a == 2:
            tu = input("Nhập từ cần tra: ")
            if tu in tu_dien.keys():
                print(f"{tu} có nghĩa là: ",tu_dien[tu])
            else:
                print("Không tìm thấy trong từ điển")
        if a == 3:
            new_word = input("Nhập từ tiếng Anh: ")
            new_mean = input("Nhập nghĩa Việt: ")
            tu_dien[new_word] = new_mean
            print("Dictionary:", tu_dien)
        if a == 4:
            del_word = input("Nhập từ cần xóa: ")
            ask = int(input("Bạn có thật sự muốn xóa hay không? 1: Xóa, 0: Không"))
            if ask == 1:
                del tu_dien[del_word]
                print("Đã xóa từ trong từ điển")
                print("Dictionary: ",tu_dien) 
        b = int(input("Tiếp tục lựa chọn? 1: Có, 0: Không"))    