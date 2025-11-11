# W2A12: 
# Nhập độ dài cạnh n
n = int(input("Nhập độ dài cạnh Rubik (n): "))

# Số miếng dán trên 1 mặt là n*n
mieng_dan_mot_mat = n ** 2
# Khối lập phương có 6 mặt
tong_mieng_dan = mieng_dan_mot_mat * 6

# In ra tổng số miếng dán
print(tong_mieng_dan)