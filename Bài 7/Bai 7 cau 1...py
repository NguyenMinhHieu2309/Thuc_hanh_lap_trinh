print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import os

# Tự động tạo file a.txt ngay cùng thư mục với file .py 
filename = 'a.txt'

if not os.path.exists(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Dòng 1\nDòng 2\nDòng 3\nDòng cuối cùng\n')
    print("Đã tự động tạo file a.txt để test!")

# Đọc và in ngược thứ tự các dòng
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in reversed(lines):
        print(line, end='')
