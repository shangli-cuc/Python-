#绘制彩色螺旋线colors_spiral_line.py

import turtle
turtle.tracer(False)#不需要等待直接出图
turtle.bgcolor("black")
color=["red","yellow","violet","blue"]
for i in range (400):
    turtle.forward(i*2)
    turtle.color(color[i%4])
    turtle.left(91)
turtle.tracer(True)
