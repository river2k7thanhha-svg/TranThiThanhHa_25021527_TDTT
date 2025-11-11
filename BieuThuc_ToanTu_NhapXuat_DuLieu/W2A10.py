# W2A10: 
# Nhập tên 3 người trên một dòng, cách nhau bởi dấu cách
input_ten = input("Nhập tên 3 người (cách nhau bởi dấu cách, VD: Bob Alice Helen): ")
# Tách chuỗi thành danh sách các tên
danh_sach_ten = input_ten.split()

# Đảo ngược danh sách tên
danh_sach_ten.reverse()

# Lấy tên người cuối (vị trí 0 sau khi đảo ngược)
ten_cuoi = danh_sach_ten[0]
# Lấy tên hai người đầu (vị trí 1 và 2 sau khi đảo ngược)
ten_dau_tien = danh_sach_ten[1]
ten_thu_hai = danh_sach_ten[2]

# Định dạng output: "Hi [Tên cuối], [Tên thứ hai] and [Tên đầu tiên]."
output_str = f"Hi {ten_cuoi}, {ten_thu_hai} and {ten_dau_tien}."

print(output_str)