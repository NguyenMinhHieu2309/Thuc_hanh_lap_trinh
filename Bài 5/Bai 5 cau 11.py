print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
import numpy as np

# Dữ liệu đầu vào
data = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Định nghĩa kiểu dữ liệu cấu trúc
dtype = [('name', 'U20'), ('class', 'i4'), ('height', 'f4')]

# Tạo structured array
arr = np.array(data, dtype=dtype)

# Sắp xếp theo lớp trước, sau đó theo chiều cao
sorted_arr = np.sort(arr, order=['class', 'height'])

print(sorted_arr)
