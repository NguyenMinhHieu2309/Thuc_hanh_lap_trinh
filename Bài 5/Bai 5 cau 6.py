print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
# Module hàm 
def sort_list(arr):
    return sorted(arr)

def find_max(arr):
    return max(arr)

def find_min(arr):
    return min(arr)

def find_positions(arr, value):
    """Trả về danh sách vị trí xuất hiện của value"""
    return [i for i, v in enumerate(arr) if v == value]


# Chương trình chính 
print("Nhập danh sách số (ví dụ: 1,2,3,4,5)")
raw = input("Nhập danh sách: ")

# Tách chuỗi thành list số
lst = [float(x) for x in raw.split(",")]

# Gọi hàm
sorted_list = sort_list(lst)
max_value = find_max(lst)
min_value = find_min(lst)

# Tìm vị trí (index)
max_positions = find_positions(lst, max_value)
min_positions = find_positions(lst, min_value)

# ===== In kết quả =====
print("\n--- Kết quả ---")
print("Danh sách sau khi sắp xếp:", sorted_list)
print("Phần tử lớn nhất:", max_value)
print("Vị trí phần tử lớn nhất:", max_positions)

print("Phần tử nhỏ nhất:", min_value)
print("Vị trí phần tử nhỏ nhất:", min_positions)
