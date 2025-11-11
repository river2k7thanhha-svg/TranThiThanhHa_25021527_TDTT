# W2A3: 
# Nhập hai số nguyên a và b 
# Dùng input().split() để nhập 2 số trên 1 dòng cách nhau bởi khoảng trắng
a, b = map(int, input("Nhập hai số nguyên a và b (cách nhau bởi dấu cách): ").split())

# Tính toán
tong = a + b
hieu = a - b
tich = a * b
phan_nguyen = a // b  # Phép chia lấy phần nguyên
phan_du = a % b      # Phép chia lấy phần dư
chia_thuc = a / b    # Phép chia thực

# In ra kết quả 
print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Phần nguyên:", phan_nguyen)
print("Phần dư:", phan_du)
# Kết quả chia thực lấy đến 2 chữ số thập phân
print(f"Chia thực: {chia_thuc:.2f}")