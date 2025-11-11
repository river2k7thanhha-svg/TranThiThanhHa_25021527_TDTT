# W2A11:
# Nhập giờ (h) và phút (m)
h, m = map(int, input("Nhập số giờ và số phút (cách nhau bởi dấu cách): ").split())

# Tính tổng số giây
# 1 giờ = 3600 giây, 1 phút = 60 giây
tong_giay = h * 3600 + m * 60

# In ra kết quả
print(tong_giay)