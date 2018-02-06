#dictionary_turtle.py
#字典的应用，统计英文单词词频，画出柱状图

import turtle
count=10#单词排序显示的个数，只显示前十的单词
data=[]#y轴数据，单词频率
words=[]#x轴数据，单词数组
yScale=6#y轴显示放大倍数
xScale=30#x轴显示放大倍数
def processfile(line,wordcount):
    
    line=replacepunctuation(line)
    words=line.split()
    for word in words:
        if word in wordcount:
            wordcount[word]+=1
        else:
            wordcount[word]=1
def replacepunctuation(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line=line.replace(ch," ")
    return line

#绘制线条
def drawline(t,x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)

#绘制文字
def drawtext(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)

#绘制柱体
def drawbar(t):
    for i in range(count):
        drawrectangle(t,i+1,data[i])
def drawrectangle(t,x,y):
    x*=xScale
    y*=yScale
    drawline(t,x-5,0,x-5,y)
    drawline(t,x-5,y,x+5,y)
    drawline(t,x+5,y,x+5,0)
    #drawline(t,x+5,0,x-5,0)
    
#绘制统计图
def drawgraph(t):
    drawline(t,0,0,360,0)
    drawline(t,0,300,0,0)

    for x in range(count):
        x+=1
        drawtext(t,x*xScale-4,-20,words[x-1])
        drawtext(t,x*xScale-4,data[x-1]*yScale+10,data[x-1])
        
    drawbar(t)
    
def main():
    file=open("E:\\英语\\the information age_the Internet\\1.txt","r")
    wordcount={}
    for line in file:
        processfile(line.lower(),wordcount)
    #pairs=wordcount.items()
    #python字典的items方法返回以列表形式返回字典的（键、值）对的元组形式的数组
    pairs=list(wordcount.items())
    #list方法将元组转换成列表，元组是小括号()，列表是中括号[]，字典是大括号{}
    #print(pairs)
    items=[[x,y] for [y,x] in pairs]
    items.sort()
    #print(items)
    for i in range(len(items)-1,len(items)-1-count,-1):
        print(items[i][1]+"\t"+str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
    file.close()
    
    #根据词频绘制柱状图
    turtle.title("词频结果柱状图")
    turtle.setup(900,750,0,0)
    t=turtle.Turtle()
    t.hideturtle()
    t.pensize(3)
    drawgraph(t)
main()

