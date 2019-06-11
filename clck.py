import circle as c
import rotate
import time
from turtle import *
import turtle
import dd
turtle.penup()
t=turtle.Turtle()
t.penup()
r=100
c.circle(r)
x1=0
x2=0
y1=0
y2=r
o=0
r1=rotate.rotate(0,0,o+330,x1,y1,x2,y2)
r2=rotate.rotate(0,0,o+300,x1,y1,x2,y2)
turtle.penup()
t.goto(x2,y2)
t.write("12",False, "center",font=("Arial", 10, "normal"))
t.goto(r1[0][1],r1[1][1])
t.write("1",False, "center",font=("Arial", 10, "normal"))
t.goto(r2[0][1],r2[1][1])
t.write("2",False, "center",font=("Arial", 10, "normal"))
t.goto(y2,x1)
t.write("3",False, "center",font=("Arial", 10, "normal"))
t.goto(r2[0][1],-r2[1][1])
t.write("4",False, "center",font=("Arial", 10, "normal"))
t.goto(r1[0][1],-r1[1][1])
t.write("5",False, "center",font=("Arial", 10, "normal"))
t.goto(x1,-y2)
t.write("6",False, "center",font=("Arial", 10, "normal"))
t.goto(-r1[0][1],-r1[1][1])
t.write("7",False, "center",font=("Arial", 10, "normal"))
t.goto(-r2[0][1],-r2[1][1])
t.write("8",False, "center",font=("Arial", 10, "normal"))
t.goto(-y2,x1)

t.write("9",False, "center",font=("Arial", 10, "normal"))
t.goto(-r2[0][1],r2[1][1])

t.write("10",False, "center",font=("Arial", 10, "normal"))
t.goto(-r1[0][1],r1[1][1])
t.write("11",False, "center",font=("Arial", 10, "normal"))
astamp = t.stamp()
clearstamp(stamp)
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()

k=0
t4=turtle.Turtle()
astamp = turtle.stamp()
clearstamp(stamp)
s = Shape("compound")
k=Shape("compound")
poly1 = ((0,0),(0,7),(-r,7))
k.addcomponent(poly1,"red", "blue")
s.addcomponent(poly1, "red", "blue")
poly2 = ((-r,15),(-r,15),(-r-15,0),(-r-15,5))
s.addcomponent(poly2, "green", "blue")
register_shape("myextrashape",s)
register_shape("myshape", k)
t1.shape("myextrashape")
t1.goto(0,0)
t1.penup()
t1.seth(0)
t2.goto(0,0)
t2.penup()
t2.seth(0)
t3.goto(0,0)
t3.penup()
t3.seth(0)
t4.penup()
t2.shape("myshape")
t3.shape("myshape")
a=6
t4.ht()
t.ht()
turtle.ht()
while True:
    for i in range(0,60):
        time.sleep(1)
        #c=rotate.rotate(0,0,-i*a,x1,y1,x2,r)
        t1.right(6)
        t2.right(1/10)
        t3.right(1/625)
       
        
      
 
        
        
bye()      


        
