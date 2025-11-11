# W2A14:
# Nhập hai số a và b
a, b = map(int, input("Nhập hai số a và b (cách nhau bởi dấu cách): ").split())

print(f"Giá trị ban đầu: a = {a}, b = {b}")

# Hoán đổi giá trị bằng phương pháp không dùng biến phụ (phép cộng/trừ hoặc phép XOR)
# Dùng phép cộng và trừ:
# a = a + b   # a giữ tổng cũ của a và b
# b = a - b   # b = (a + b) - b = a (Giá trị a cũ)
# a = a - b   # a = (a + b) - a (Giá trị b cũ)

# Hoặc dùng cú pháp hoán đổi trực tiếp của Python (thực chất là một cách viết gọn, không khai báo biến tường minh)
a, b = b, a

print(f"Giá trị sau khi hoán đổi: a = {a}, b = {b}")