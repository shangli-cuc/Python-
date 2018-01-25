#draw_seven_seg_display_version2.py
#将当前时刻用七段数码管的形式打印出来，有数码管间隔
import turtle
import time
def drawgap():
    turtle.penup()
    turtle.forward(5)
def drawline(boolean):
    drawgap()
    turtle.pendown() if boolean else turtle.penup()
    turtle.forward(40)
    drawgap()
    turtle.right(90)
def drawdigit(i):
    drawline(True) if i in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if i in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if i in [0,2,3,5,6,8] else drawline(False)
    drawline(True) if i in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if i in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if i in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if i in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.forward(20)
def drawdate(now_time):
    for i in now_time:
        turtle.color("red")
        if i=="+":
            turtle.write("年",font=("Arial",15))
            turtle.forward(20)
        elif i=="=":
            turtle.write("月",font=("Arial",15))
            turtle.forward(20)
        elif i=="-":
            turtle.write("日",font=("Arial",15))
            turtle.forward(20)
        elif i=="_":
            turtle.write("时",font=("Arial",15))
            turtle.forward(20)
        elif i=="!":
            turtle.write("分",font=("Arial",15))
            turtle.forward(20)
        elif i=="*":
            turtle.write("秒",font=("Arial",15))
            turtle.forward(20)
        else:
            turtle.color("black")
            drawdigit(eval(i))
def main():
    turtle.setup(1500,350,200,200)
    turtle.tracer(False)
    turtle.penup()
    turtle.forward(-550)
    turtle.pensize(5)
    now_time=time.strftime("%Y+%m=%d-%H_%M!%S*",time.localtime())
    drawdate(now_time)
main()
