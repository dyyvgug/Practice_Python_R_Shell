#PythonDraw.py
import turtle as t
t.setup(650,350,200,200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor(1,0.96,0.93)
t.seth(-40)
for i in range(2):
    t.circle(40,80)
    t.circle(-40,80)
t.pencolor("blue")
for i in range(2):
    t.circle(40, 80)
    t.circle(-40, 80)
t.pencolor("purple")
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40 * 2/3)
t.right(45)
t.circle(40,40)
t.done()
