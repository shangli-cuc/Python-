#绘制螺旋线spiral_line.py

import turtle
turtle.tracer(False)#设置画图的延迟，false表示直接得出图像，不需要等待
turtle.color("black")
turtle.speed(10)
turtle.pensize(2)
turtle.seth(90)
for i in range (100):
    turtle.forward(i*2)
    turtle.left(90)
turtle.tracer(True)#有这一步，最后会有画笔箭头
