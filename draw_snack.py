#turtle
#使用turtle module 画出snack图形

import turtle

def drawSnack(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)#rad大于0圆圈在turtle的左侧，反之在右侧
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.forward(rad)#turlte.fd()画直线
    turtle.circle(neckrad+1,180)
    turtle.forward(rad*2/3)
    
def main():
    #初始化一个1300*800的窗口，窗口起点从屏幕左上角开始，坐标0*0
    turtle.setup(1300,800,0,0)
    pythonsize=30 
    turtle.pensize(pythonsize) #线条的宽度
    turtle.pencolor("blue") #线条的颜色，采用RGB绘色方式定义"#0000FF"为蓝色
    turtle.seth(-40) #setheading设置turtle起始地角度值
    drawSnack(40,80,5,pythonsize/2) #半径 角度 循环次数 蛇头半径

main()
    
'''
turtle.setup(1300,800,0,0)
turtle.pensize(30)
turtle.seth(-40)
for i in range (5):
    turtle.circle(40,80)
    turtle.seth(-40)
'''

    
    
