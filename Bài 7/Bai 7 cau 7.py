print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

with open('a.txt', 'r', encoding='utf-8') as f:
    so_dong = len(f.readlines())   # Đọc hết → đếm số phần tử trong list

print("Số dòng trong file là:", so_dong)
