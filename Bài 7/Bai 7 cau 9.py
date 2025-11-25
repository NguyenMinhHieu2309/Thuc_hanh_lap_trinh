print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

# Sao chép từ file nguồn sang file đích
with open('a.txt', 'r', encoding='utf-8') as nguon:
    noidung = nguon.read()

with open('b.txt', 'w', encoding='utf-8') as dich:
    dich.write(noidung)

print("Đã sao chép thành công từ a.txt sang b.txt!")
