# W2A4: 
# Nhập 6 đầu điểm trên một dòng, cách nhau bởi dấu cách
# map(float, ...) để đảm bảo các đầu điểm có thể là số thực
a1, b1, c1, a2, b2, a3 = map(float, input("Nhập 6 đầu điểm (cách nhau bởi dấu cách): ").split())

# Công thức tính điểm trung bình
# TB = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
diem_tb = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10

# In ra kết quả làm tròn đến 1 chữ số phần thập phân
print(f"Điểm trung bình: {diem_tb:.1f}")