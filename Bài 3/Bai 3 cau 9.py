print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
# === SIMPLE CALCULATOR ===

# 1. Hàm cộng
def add(x, y):
    return x + y

# 2. Hàm trừ
def subtract(x, y):
    return x - y

# 3. Hàm nhân
def multiply(x, y):
    return x * y

# 4. Hàm chia
def divide(x, y):
    if y == 0:
        return "Lỗi: Không thể chia cho 0!"
    return x / y

# === Chương trình chính ===
print("=== MÁY TÍNH ĐƠN GIẢN ===")
print("Chọn phép toán:")
print("1. Cộng (+)")
print("2. Trừ (-)")
print("3. Nhân (*)")
print("4. Chia (/)")

# Nhập lựa chọn
while True:
    choice = input("\nNhập lựa chọn (1/2/3/4): ").strip()
    if choice in ['1', '2', '3', '4']:
        break
    print("Lỗi: Vui lòng nhập số từ 1 đến 4!")

# Nhập 2 số
try:
    num1 = float(input("Nhập số thứ nhất: "))
    num2 = float(input("Nhập số thứ hai: "))
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ!")
    exit()

# Xử lý phép toán
if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")

elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")

elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")

elif choice == '4':
    result = divide(num1, num2)
    if isinstance(result, str):  # Nếu là lỗi
        print(result)
    else:
        print(f"{num1} / {num2} = {result}")
