print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

def binary_search(lst, value):
    lowerBound = 0
    upperBound = len(lst) - 1

    while lowerBound <= upperBound:
        midPoint = (lowerBound + upperBound) // 2
        
        if lst[midPoint] < value:
            lowerBound = midPoint + 1
        elif lst[midPoint] > value:
            upperBound = midPoint - 1
        else:
            return True  # tìm thấy

    return False  # không tìm thấy

def binary_search(lst, value):
    lowerBound = 0
    upperBound = len(lst) - 1

    while lowerBound <= upperBound:
        midPoint = (lowerBound + upperBound) // 2
        
        if lst[midPoint] < value:
            lowerBound = midPoint + 1
        elif lst[midPoint] > value:
            upperBound = midPoint - 1
        else:
            return True

    return False

# Chương trình chính

n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)

lst.sort()
print("Danh sách sau khi sắp xếp:", lst)

value = int(input("Nhập giá trị cần tìm: "))

if binary_search(lst, value):
    print("Tồn tại trong danh sách!")
else:
    print("Không tồn tại trong danh sách!")

