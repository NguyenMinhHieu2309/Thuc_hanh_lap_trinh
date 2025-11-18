print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
def bubbleSort(nlist):
    loop = len(nlist)
    for i in range(loop - 1):
        swapped = False
        for j in range(loop - 1 - i):
            if nlist[j] > nlist[j + 1]:
                # hoán đổi
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        # nếu không có hoán đổi => mảng đã sắp xếp
        if not swapped:
            break
    return nlist


# Nhập danh sách từ bàn phím

arr = list(map(int, input("Nhập các phần tử: ").split()))

print("Kết quả sau khi sắp xếp:")
print(bubbleSort(arr))
