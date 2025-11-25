print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

def ghi_va_doc_file():
    # Bước 1: Ghi nội dung vào file
    with open('abc.txt', 'w', encoding='utf-8') as f:
        f.write("Python Exercises\n")
        f.write("Java Exercises")
    
    # Bước 2: Đọc lại và in ra
    with open('abc.txt', 'r', encoding='utf-8') as f:
        noidung = f.read()
        print(noidung)

# Gọi hàm để chạy
ghi_va_doc_file()
