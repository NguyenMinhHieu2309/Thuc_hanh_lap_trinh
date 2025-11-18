print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
def Sequential_Search(dlist, item):
    pos = 0
    found = False

    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1
    return found, pos


# Chương trình chính

n = int(input("Nhập số lượng phần tử: "))
dlist = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(x)

item = int(input("Nhập phần tử cần tìm: "))

found, pos = Sequential_Search(dlist, item)

if found:
    print(f"Tìm thấy {item} tại vị trí {pos}")
else:
    print(f"Không tìm thấy {item} trong danh sách")
