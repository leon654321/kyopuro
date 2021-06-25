#問題文
#https://atcoder.jp/contests/abc203/tasks/abc203_c

import numpy as np
import sys
input=sys.stdin.readline

#入力
N,k=map(int,input().split())

#友達のいる村ともらえるお金の配列
A=np.zeros((2,N))
for i in range(N):
    a,b=map(int,input().split())
    A[0,i]=a
    A[1,i]=b

#村のナンバーで昇順並び替え
index = np.argsort(A[0,:])
A = A[:,index]

#村の番号
num=0
#Aのindex
i=0

#お金を持ってる間進み続ける
while k>0:
    
    #k円持ってるなら村をk進む
    num+=k
    
    #番号numの村までにもらえるお金をkに加える
    k=0
    while i<N and A[0,i]<=num:
        k+=A[1,i]
        i+=1
        
print(int(num))
