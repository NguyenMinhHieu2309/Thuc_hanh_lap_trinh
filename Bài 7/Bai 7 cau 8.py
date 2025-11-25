print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

# Danh sách cần ghi vào file
danh_sach = ["Python", "Java", "C++", "JavaScript", "PHP"]

# Ghi từng phần tử vào file (mỗi phần tử 1 dòng)
with open('danhsach.txt', 'w', encoding='utf-8') as f:
    for item in danh_sach:
        f.write(item + '\n')    # thêm \n để xuống dòng

print("Đã ghi danh sách vào file danhsach.txt thành công!")
