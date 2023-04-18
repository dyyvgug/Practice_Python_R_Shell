#AutoTraceDraw.py
import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("自由轨迹数据.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
    #map(函数一，数据集）使得函数对每个数据分别进行操作
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:   #等同于datals[i][1] == Ture:  通常Ture对应1，False对应0
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()
