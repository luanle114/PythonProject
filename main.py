from function import *
##### main #####

taikhoan = [["admin","admin"], ["user","user"]]
donhang =[]
checkUser = False
checkAdmin = False
file_path = 'data_sanpham.txt'

print("+----------------------------------------------+")
print("|        CHÀO MỪNG ĐẾN TẠP HÓA MÈO BÉO         |")
print("+----------------------------------------------+")
print("\n\n")

print("+------------------DANG NHAP-------------------+")
tamp_check = True
while (tamp_check):
    username_login = input("UserName : ")
    for login in taikhoan:
        if(username_login == login[0]):
            password_login = input("Password : ")
            if(password_login == login[1]):
                print("Đăng nhập thành công")
                if(username_login == "admin"):
                    checkAdmin = True
                    checkUser = False
                    tamp_check = False
                else:
                    checkUser = True
                    checkAdmin = False
                    tamp_check = False
                print("\n\n")
    if(tamp_check == True):
        print("Không thấy tài khoản\n")
        print("+----------------------------------------------+\n\n")




data_sanpham = read_data_from_file(file_path)
while checkAdmin:
    print("+----------------------------------------------+")
    print("| 1. Hiển thị danh sách sản phẩm               |")
    print("| 2. Chỉnh sửa danh sách sản phẩm              |")
    print("| 3. Đặt hàng                                  |")
    print("| 4. Chỉnh sửa sản phẩm trong đơn hàng         |")
    print("| 5. Hiển thị đơn hàng                         |")
    print("| 6. Xác nhận đơn hàng                         |")
    print("| 0. Thoát                                     |")
    print("+----------------------------------------------+")
    choose = str(input("Vui lòng nhập mã hành động :  "))

    if choose == "1" or choose == "một":
        output_sanpham(data_sanpham)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")
    elif choose == "2" or choose == "hai":
        output_sanpham(data_sanpham)
        edit_product_by_id(file_path,data_sanpham)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")
    elif choose == "3" or choose == "ba":
        output_sanpham(data_sanpham)
        donhang = input_donhang(data_sanpham)
        output_sanpham(donhang)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")        
    elif choose == "4" or choose == "bốn":
        output_sanpham(donhang)
        donhang = edit_donhang(donhang)
        if donhang == 0:
            donhang = []
        output_sanpham(donhang)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")        
    elif choose == "5" or choose == "năm":
        output_sanpham(donhang)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")        
    elif choose == "6" or choose == "sáu":
        output_sanpham(donhang)
        donhang = thanhtoan_donhang(donhang)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")        
    elif choose == "0" or choose == "không":
        checkAdmin = False
        print("\n\n\n\n\n\n+----------------------------------------------+")
        print("|                                              |")
        print("|  CẢM ƠN BẠN ĐÃ DÙNG DỊCH VỤ CỦA CHÚNG TÔI    |")
        print("|                                              |")
        print("+----------------------------------------------+\n\n\n\n\n\n")
    else:
        print("NHẬP SAI *** YÊU CẦU NHẬP LẠI !!")   

while checkUser:
    print("+----------------------------------------------+")
    print("| 1. Hiển thị danh sách sản phẩm               |")
    print("| 2. Đặt hàng                                  |")
    print("| 3. Chỉnh sửa sản phẩm trong đơn hàng         |")
    print("| 4. Hiển thị đơn hàng                         |")
    print("| 5. Xác nhận đơn hàng                         |")
    print("| 0. Thoát                                     |")
    print("+----------------------------------------------+")
    choose = str(input("Vui lòng nhập mã hành động :  "))

    if choose == "1" or choose == "một":
        output_sanpham(data_sanpham)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")
    elif choose == "2" or choose == "hai":
        output_sanpham(data_sanpham)
        donhang = input_donhang(data_sanpham)
        output_sanpham(donhang)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")        
    elif choose == "3" or choose == "ba":
        output_sanpham(donhang)
        donhang = edit_donhang(donhang)
        output_sanpham(donhang)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")        
    elif choose == "4" or choose == "bốn":
        output_sanpham(donhang)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")        
    elif choose == "5" or choose == "năm":
        output_sanpham(donhang)
        donhang = thanhtoan_donhang(donhang)
        a = input("\nNhấn phím bất kì để trở về menu : ")
        print("\n\n\n\n\n\n\n\n\n\n")        
    elif choose == "0" or choose == "không":
        checkUser = False
        print("\n\n\n\n\n\n+----------------------------------------------+")
        print("|                                              |")
        print("|  CẢM ƠN BẠN ĐÃ DÙNG DỊCH VỤ CỦA CHÚNG TÔI    |")
        print("|                                              |")
        print("+----------------------------------------------+\n\n\n\n\n\n")
    else:
        print("NHẬP SAI *** YÊU CẦU NHẬP LẠI !!")   

    

