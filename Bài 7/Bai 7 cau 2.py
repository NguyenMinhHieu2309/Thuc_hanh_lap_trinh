print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")


with open('a.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()          # Đọc tất cả dòng

lc = len(lines)                    # Số dòng
wc = 0                             # Số từ
cc = 0                             # Số ký tự (không tính khoảng trắng và xuống dòng)

for line in lines:
    cc += len(line.replace(' ', '').replace('\n', '').replace('\t', ''))
    # Cách khác: cc += len(line.strip()) nếu chỉ muốn đếm ký tự hiển thị
    
    words = line.strip().split()   # Tách từ theo khoảng trắng
    wc += len(words)

print(f"The no. of chars is {cc}\nThe no. of words is {wc}\nThe no. of lines is {lc}")
