import math
import dd
from turtle import *
def rotate(tx,ty,o,x1,y1,x2,y2):
    if(o<0):
        o=360+o
    
    t=[[1,0,tx],[0,1,ty],[0,0,1]]

    sum1=0
    sume=0        

    er=[[0,0,0],[0,0,0],[0,0,0]]
    final=[[0,0,0],[0,0,0],[0,0,0]]

    cos=math.cos(math.pi/180*o)
    sin=math.sin(math.pi/180*o)
    if(0<cos < 0.0000000000001):
        cos=0
    if(0<sin < 0.0000000001):
        sin=0
    r=[[cos,(-1)*sin,0],[sin,cos,0],[0,0,1]]

    it=[[1,0,(-1)*tx],[0,1,(-1)*ty],[0,0,1]]
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
            
                sum1=sum1+(t[i][k]*r[k][j])
            
                
            er[i][j]=sum1
            sum1=0




    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                sume=sume+(er[i][k]*it[k][j])
            final[i][j]=sume
            sume=0
    
    points=[[x1,x2,1],[y1,y2,1]]

    f=[[0,0],[0,0],[0,0]]

    sumei=0
    for i in range(0,3):
        for j in range(0,2):
            for k in range(0,2):
                sumei=sumei+(final[i][k]*points[k][j])
            f[i][j]=sumei
            sumei=0
    return f

'''dd.dd1(0,0,0,100)
f=rotate(0,0,90,0,0,0,100)
import time
time.sleep(1)
penup()
dd.dd1(int(f[0][0]),int(f[1][0]),int(f[0][1]),int(f[1][1]))'''
