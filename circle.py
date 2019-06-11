from turtle import *
import time
reset()
penup()

def circle(r):
    
    xk=0
    yk=r
    pk=1-r
    l=[]
    while(xk<=yk):
        if(pk<0):
            l.append([xk,yk])      
            xk=xk+1
            yk=yk
            pk=pk+2*xk+1
        else:
            l.append([xk,yk])
            xk=xk+1
            yk=yk-1
            pk=pk+2*xk-2*yk+1
    for x,y in l:
        goto(x,y)
        pendown()
    for i in range(len(l)-1,-1,-1):
        x,y=l[i]
        goto(y,x)
    for i in range(0,len(l)-1):
        x,y=l[i]
        goto(y,-x)
    for i in range(len(l)-1,-1,-1):
        x,y=l[i]
        goto(x,-y)
    for i in range(0,len(l)-1):
        x,y=l[i]
        goto(-x,-y)
    for i in range(len(l)-1,-1,-1):
        x,y=l[i]
        goto(-y,-x)
    for i in range(0,len(l)-1):
        x,y=l[i]
        goto(-y,x)
    for i in range(len(l)-1,-1,-1):
        x,y=l[i]
        goto(-x,y)
    return r


