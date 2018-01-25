#draw_seven_seg_display_version1.py
#将当前年月日用七段数码管的形式打印出来，没有数码管的间隔
import turtle
import time
def drawline(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.forward(40)
    turtle.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)#有中间那一横的数字
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)#
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.forward(20)
def drawdate(now_time):
    for i in now_time:
        drawdigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    #turtle.speed(1)
    turtle.tracer(False)
    turtle.penup()
    turtle.forward(-300)
    turtle.pensize(5)
    now_time=time.strftime("%Y%m%d",time.localtime())
    drawdate(now_time)
    turtle.hideturtle()
    #turtle.tracer(True)
main()
