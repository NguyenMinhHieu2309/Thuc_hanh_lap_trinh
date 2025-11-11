print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
def checkValue(n):
    if n % 2 == 0:
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")


try:
    num = int(input("Nhập một số nguyên: "))
    checkValue(num)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
