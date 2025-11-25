print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(1, 180):          # sửa từ range(1,180) để tránh lỗi
    painter.left(18)              # xoay 18 độ mỗi lần (360/20 = 18, nhưng ảnh ghi 18)
    drawsq(painter, 200)

window.exitonclick()             
