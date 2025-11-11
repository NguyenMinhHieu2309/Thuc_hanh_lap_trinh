print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
def get_sum(*num):
    tmp = 0
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)
