#绘制太阳花sun_flower.py
import turtle

turtle.color("red", "yellow")#同时设置pencolor=color1, fillcolor=color2  
turtle.speed(10)#画笔的速度
turtle.begin_fill()#开始填充颜色fillcolor  
while True:
    turtle.forward(200)#前进200个像素点  
    turtle.left(170)#逆时针旋转170度
    if abs(turtle.pos())<1:#判断回到原点，停止循环
        break
turtle.end_fill()#停止填充颜色
