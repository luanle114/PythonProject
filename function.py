##### function #####

# Hàm đọc thông tin file
def read_data_from_file(file_path):
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  
            if line:  
                parts = line.split(',')
                item = (int(parts[0]), parts[1], int(parts[2]))
                data_list.append(item)
    return data_list

# Hàm out thông tin
def output_sanpham(sanpham):
    header = f"| {'Mã':<3} | {'Tên sản phẩm':<20} | {'Giá (VNĐ)':>10} |"
    separator = "+" + "-"*5 + "+" + "-"*22 + "+" + "-"*12 + "+"
    print(separator)
    print(header)
    print(separator)
    for sp in sanpham:
        row = f"| {sp[0]:<3} | {sp[1]:<20} | {sp[2]:>10} |"
        print(row)
        print(separator)

# Hàm đặt hàng
def input_donhang(sanpham):
    data_list = []
    print("\n+----------------------------------------------+\n")
    check = True
    while(check):
        idnhap = int(input("\nNhấn 0 để thoát hành động hiện tại\nNhập id sản phẩm muốn mua : "))    
        if(idnhap==0):
            check = False
        else:
            for i in sanpham:
                if(idnhap == i[0]):
                    data_list.append(i)
                    print("Xác nhận mua hàng")
                    continue
        print("\nKhông tìm thấy id sản phẩm\n")
    print("\n+----------------------------------------------+\n\n")
    return data_list

# Hàm tính tổng giá
def total_donhang(sanpham):
    total_price = 0
    for product in sanpham:
        price = product[2]
        total_price += price
    return total_price

# Hàm chỉnh sửa đặt hàng 
def edit_donhang(sanpham):
    print("\n+----------------------------------------------+\n")
    if not sanpham:
        print("Danh sách đơn hàng rỗng\n")
        return 0
    check = True
    while(check):
        idnhap = int(input("\nNhấn 0 để thoát hành động hiện tại\nNhập id sản phẩm muốn chỉnh sửa : "))    
        if(idnhap==0):
            check = False
        else:
            for i in sanpham:
                if(idnhap == i[0]):
                    sanpham.remove(i)
                    print("\nXác nhận hủy sản phẩm\n")
                    break       
            
            
    print("\n+----------------------------------------------+\n\n")
    return sanpham

# Hàm thanh toán đơn hàng
def thanhtoan_donhang(sanpham):
    print("\n+----------------------------------------------+\n")
    if not sanpham:
        print("Danh sách đơn hàng rỗng\n")
        return 0

    total = total_donhang(sanpham)
    print("\nTổng tiền cần thanh toán:",total)
    check = True
    while(check):
        idnhap = int(input("\nXác nhận thanh toán\nCó: 1\nKhông: 0\nVui lòng nhập mã hành động :  "))    
        if(idnhap==0):
           return sanpham
        elif(idnhap==1):
            print("")
            print("\n\n\n\n\n\n+----------------------------------------------+")
            print("|  THANH TOÁN THÀNH CÔNG                       |")
            print("|        CẢM ƠN BẠN                            |")
            print("|                                              |")
            print("+----------------------------------------------+\n\n\n\n\n\n")
            sanpham = []
            return sanpham
        else:
            print("NHẬP SAI HÀNH ĐỘNG YÊU CẦU NHẬP LẠI !!")  


            
    print("\n+----------------------------------------------+\n\n")
    return sanpham

# Hàm viết vô file
def write_products_to_file(filename, products):
    with open(filename, 'w', encoding='utf-8', errors='replace') as file:
        for product in products:
            safe_name = product[1].encode('utf-8', 'replace').decode('utf-8')
            file.write(f"{product[0]},{safe_name},{product[2]}\n")



# Hàm chỉnh sửa danh sách sản phẩm
def edit_product_by_id(filename, listsanpham):
    products = listsanpham
    found = False

    check = True
    while(check):
        idnhap = int(input("\nNhấn 0 để thoát hành động hiện tại\nNhập id sản phẩm muốn chỉnh sửa : "))    
        if(idnhap==0):
            check = False
            return 0
        else:
            for i, product in enumerate(products):
                if product[0] == idnhap:
                    found = True
                    print(f"Thông tin sản phẩm có ID: {idnhap}")
                    print(f"Tên sản phẩm: {product[1]}")
                    print(f"Giá sản phẩm: {product[2]}")
                    choice = input("Bạn muốn chỉnh sửa 'tên' hay 'giá' của sản phẩm này: ").lower()
                    if choice == 'tên':
                        new_name = input("Nhập tên mới: ")
                        products[i] = (idnhap, new_name, product[2])
                        print("Đã cập nhật tên sản phẩm.")
                    elif choice == 'giá':
                        new_price = int(input("Nhập giá mới: "))
                        products[i] = (idnhap, product[1], new_price)
                        print("Đã cập nhật giá sản phẩm.")
                    else:
                        print("Lựa chọn không hợp lệ.")
                    write_products_to_file(filename, products)
                    break

    if not found:
        print(f"Không tìm thấy sản phẩm có ID {idnhap}.")