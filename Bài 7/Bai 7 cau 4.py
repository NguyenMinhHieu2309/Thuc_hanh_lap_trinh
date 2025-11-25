print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")


def doc_n_dong_dau(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        for i in range(n):             # lặp n lần
            line = f.readline()        # đọc từng dòng
            if line == '':             # nếu hết file trước khi đủ n dòng
                break
            print(line, end='')        # in ra y nguyên

# Gọi hàm để test
doc_n_dong_dau('a.txt', 3)   # in ra 3 dòng đầu tiên của file a.txt
