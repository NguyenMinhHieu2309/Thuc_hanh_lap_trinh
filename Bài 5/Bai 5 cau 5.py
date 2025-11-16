print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

def sort_list(arr):
    return sorted(arr)

def find_max(arr):
    return max(arr)

def find_min(arr):
    return min(arr)


# Chương trình chính 
n = int(input("Nhập số lượng phần tử: "))

lst = []
for i in range(n):
    val = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(val)

# Gọi hàm
sorted_list = sort_list(lst)
max_value = find_max(lst)
min_value = find_min(lst)

print("Danh sách sau khi sắp xếp:", sorted_list)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)
