print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

def doc_n_dong_cuoi(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()          # Đọc hết file vào danh sách
        for line in lines[-n:]:         # Lấy n dòng cuối cùng
            print(line, end='')

# Gọi hàm để test
doc_n_dong_cuoi('a.txt', 3)   # In ra 3 dòng cuối của file a.txt
