# W2A6: 
# Nhập vào một kí tự chữ cái thường
ky_tu_thuong = input("Nhập một kí tự chữ cái thường: ")

# In ra mã Unicode (dùng hàm ord())
ma_unicode = ord(ky_tu_thuong)
print("Mã Unicode:", ma_unicode)

# Chuyển thành kí tự hoa tương ứng (dùng hàm upper() của chuỗi)
ky_tu_hoa = ky_tu_thuong.upper()
print("Kí tự hoa tương ứng:", ky_tu_hoa)