print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
import math

# Khởi tạo vị trí robot
x = 0
y = 0

print("Nhập các lệnh di chuyển (ví dụ: UP 5). Nhấn Enter không nhập gì để kết thúc.")

while True:
    command = input().strip()
    
    
    if not command:
        break
    
   
    parts = command.split()
    if len(parts) != 2:
        print("Lỗi: Nhập sai định dạng! (VD: UP 5)")
        continue
    
    direction = parts[0].upper()
    try:
        steps = int(parts[1])
    except ValueError:
        print("Lỗi: Số bước phải là số nguyên!")
        continue
    
    
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps
    else:
        print(f"Lỗi: Hướng '{direction}' không hợp lệ! Chỉ dùng UP/DOWN/LEFT/RIGHT")


print(f"\nTọa độ cuối cùng: ({x}, {y})")
distance = round(math.sqrt(x**2 + y**2))  
print(f"Khoảng cách đến gốc tọa độ: {distance}")
