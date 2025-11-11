# W2A13: 
# Nhập hai số nguyên dương a và b
a, b = map(int, input("Nhập hai số nguyên dương a và b (cách nhau bởi dấu cách): ").split())

# Tính tích
tich = a * b
# Hàng đơn vị của tích là phần dư khi chia cho 10
hang_don_vi = tich % 10

# In ra kết quả
print(hang_don_vi)