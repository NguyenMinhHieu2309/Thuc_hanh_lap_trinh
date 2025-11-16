print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
import numpy as np

# Khai báo kiểu dữ liệu cho mảng có cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu sinh viên
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.1)
]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

# Sắp xếp theo chiều cao 
print("\nSort by height:")
print(np.sort(students, order='height'))
