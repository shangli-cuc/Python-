#绘制五角星five_points_star.py

import turtle
turtle.screensize(400,400)
turtle.color("yellow","red")#画笔颜色、填充颜色
turtle.pensize(10)
turtle.begin_fill()#开始填充
for i in range (5):
    turtle.forward(200)#前进400个像素点
    turtle.right(144)#顺时针旋转144度
turtle.end_fill()#结束填充
