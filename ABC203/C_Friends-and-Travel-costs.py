#問題文
#https://atcoder.jp/contests/abc203/tasks/abc203_c

import numpy as np
import sys
#input=sys.stdin.readline
N,k=map(int,input().split())
A=np.zeros((2,N))
for i in range(N):
    a,b=map(int,input().split())
    A[0,i]=a
    A[1,i]=b
index = np.argsort(A[0,:])
A = A[:,index]
num=0
i=0
while k>0:
    num+=k
    k=0
    while i<N and A[0,i]<=num:
        k+=A[1,i]
        i+=1
print(int(num))
