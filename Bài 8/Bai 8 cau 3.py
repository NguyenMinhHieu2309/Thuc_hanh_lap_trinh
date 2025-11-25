print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import turtle
import random

# Danh sách màu đẹp
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime"]

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("white")        # nền trắng cho nổi hoa
screen.title("Bông Hoa 10 Cánh Siêu Đẹp")

# Tạo con rùa
t = turtle.Turtle()
t.speed(0)                     # vẽ nhanh nhất
t.pensize(4)                   # nét đậm đẹp

# Đưa rùa về tâm
t.penup()
t.goto(0, 0)
t.pendown()

# VẼ BÔNG HOA 10 CÁNH ĐẸP NHƯ ẢNH
for i in range(10):
    t.pencolor(random.choice(colors))   # mỗi cánh một màu ngẫu nhiên
    t.circle(120)                       # vẽ hình tròn bán kính 120
    t.left(36)                          # xoay trái đúng 36 độ → 10 cánh đều hoàn hảo

# Ẩn con rùa và giữ cửa sổ
t.hideturtle()
screen.exitonclick()
print("Đã vẽ xong bông hoa 10 cánh siêu đẹp! Click để thoát.")
