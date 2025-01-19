import sqlite3
conn = sqlite3.connect('product.db')
print("Open database successfully")
i = int(input('''Bạn muốn làm gì?
              \n1. Hiển thị danh sách sản phẩm 
              \n2. Thêm sản phẩm mới
              \n3. Tìm kiếm sản phẩm theo tên
              \n4. Cập nhật sản phẩm
              \n5. Xóa sản phẩm '''))
k = 1
while k == 1:
    if i == 1:
        cursor = conn.execute("SELECT id, name, price, quantity from PRODUCT")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("PRICE = ", row[2])
            print("QUANTITY = ", row[3], "\n")
        print("Operation done successfully")
    elif i == 2:
        idmax = conn.execute("SELECT MAX(ID) FROM PRODUCT").fetchone()[0]
        name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập giá: "))
        quantity = int(input("Nhập số lượng: "))
        conn.execute("INSERT INTO PRODUCT (ID, NAME, PRICE, QUANTITY) VALUES (?, ?, ?, ?)", (idmax + 1, name, price, quantity))
        conn.commit()
        print("Records created successfully")
    elif i == 3:
        name = input("Nhập tên sản phẩm cần tìm (có thể nhập từ khóa): ")
        cursor = conn.execute("SELECT id, name, price, quantity FROM PRODUCT WHERE NAME LIKE ?", (f"{name}%",))
        rows = cursor.fetchall()
        if rows:
            print("Kết quả tìm kiếm:")
            for row in rows:
                print(f"ID = {row[0]}, NAME = {row[1]}, PRICE = {row[2]}, QUANTITY = {row[3]}")
        else:
            print("Không tìm thấy sản phẩm phù hợp.")
        print("Operation done successfully")
    elif i == 4:
        id = int(input("Nhập ID sản phẩm cần cập nhật: "))
        name = input("Nhập tên sản phẩm mới: ")
        price = float(input("Nhập giá mới: "))
        quantity = int(input("Nhập số lượng mới: "))
        conn.execute("UPDATE PRODUCT SET NAME = ?, PRICE = ?, QUANTITY = ? WHERE ID = ?", (name, price, quantity, id))
        conn.commit()
        print("Records updated successfully")
    elif i == 5:
        id = int(input("Nhập ID sản phẩm cần xóa: "))
        conn.execute("DELETE from PRODUCT where ID = ?", (id,))
        conn.commit()
        print("Records deleted successfully")
    else:
        print("Invalid input")
    
    k = int(input("Bạn có muốn tiếp tục không? (1: có, 0: không)"))
    i = int(input('''Bạn muốn làm gì?
              \n1. Hiển thị danh sách sản phẩm 
              \n2. Thêm sản phẩm mới
              \n3. Tìm kiếm sản phẩm theo tên
              \n4. Cập nhật sản phẩm
              \n5. Xóa sản phẩm '''))
    
conn.close()
