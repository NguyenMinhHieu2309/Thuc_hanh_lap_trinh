print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import turtle
import random

# Danh sách màu sắc
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Tạo rùa và cài đặt
painter = turtle.Turtle()
painter.shape("turtle")
painter.pensize(3)
painter.speed(10)          # vẽ nhanh hơn, đẹp hơn

# Vẽ 10 hình tròn nhiều màu
for i in range(10):
    color = random.choice(colors)    # chọn màu ngẫu nhiên
    painter.pencolor(color)          # đổi màu bút
    painter.circle(100)              # vẽ hình tròn bán kính 100
    painter.right(30)                # xoay phải 30 độ (thay vì left 60 như ảnh)
    painter.left(60)                 # xoay trái 60 độ → tổng xoay 36 độ mỗi lần
    painter.setposition(0, 0)        # quay lại tâm để vẽ chồng lên nhau

# Giữ cửa sổ mở
turtle.done()
