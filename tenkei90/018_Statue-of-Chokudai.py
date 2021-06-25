#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_r

import sys
input=sys.stdin.readline
from math import degrees,sin,cos,atan,sqrt,pi


#入力
T=int(input())
L,X,Y=map(int,input().split())
q=int(input())


for _ in range(q):
    e=int(input())
    #x=X
    
    #e分後のy座標、z座標
    y=-(L/2)*sin(e/T*2*pi)-Y
    z=(L/2)*(1-cos(e/T*2*pi))
    
    ans=degrees(atan(z/sqrt(X**2+y**2)))
    print(ans)
