print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
import re


password = input("Nhập mật khẩu: ")


errors = []


if len(password) < 6 or len(password) > 12:
    errors.append("Độ dài mật khẩu phải từ 6 đến 12 ký tự.")


if not re.search(r'[a-z]', password):
    errors.append("Mật khẩu phải chứa ít nhất 1 chữ cái thường (a-z).")


if not re.search(r'[A-Z]', password):
    errors.append("Mật khẩu phải chứa ít nhất 1 chữ cái in hoa (A-Z).")


if not re.search(r'[0-9]', password):
    errors.append("Mật khẩu phải chứa ít nhất 1 chữ số (0-9).")


if not re.search(r'[\$@#]', password):
    errors.append("Mật khẩu phải chứa ít nhất 1 trong các ký tự: $ @ #")


if errors:
    print("Mật khẩu không hợp lệ:")
    for error in errors:
        print("- " + error)
else:
    print("Mật khẩu hợp lệ!")
