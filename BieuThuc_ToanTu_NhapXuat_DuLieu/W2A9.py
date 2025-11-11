# W2A9: 
# Nhập giá đồng hồ x (USD)
x = float(input("Nhập giá đồng hồ (x USD): "))

# Phí vận chuyển cố định
phi_van_chuyen = 10 

# Thuế xuất nhập cảnh: 30% của giá x
thue_xuat_nhap_canh = x * 0.30

# Thuế VAT: 10% của giá x
thue_vat = x * 0.10

# Tổng số tiền phải trả
tong_tien = x + phi_van_chuyen + thue_xuat_nhap_canh + thue_vat

# In ra tổng số tiền làm tròn đến hai chữ số thập phân
print(f"Tổng số tiền phải trả (USD): {tong_tien:.2f}")