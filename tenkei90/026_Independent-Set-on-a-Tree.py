#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_z

import sys
from collections import deque

"""
木の性質上、あるAに属する一点から出発して隣の点をBに加える。さらにその隣をAに加える。以下を繰り返せば
AかBのどちらかはN/2頂点以上になるので出力すればよい。BFSで探索
"""

#入力
N=int(input())
A=set([]) #上記のAグループをまとめる
B=set([]) #上記のBグループをまとめる
al=set([]) #すでに訪れた点
d=deque([]) #探索する点

#グラフ生成
G=[[] for i in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

#点0からスタート
d.append(0)
al.add(0)
A.add(1)

#AとBの切り替わりをa=0,1で管理
a=0
while d:
    if a==0:
        a=1
    else:
        a=0
    L=len(d)
    for i in range(L):
        D=d.popleft()
        for j in G[D]:
            if a==0:
                if j+1 not in A:
                    d.append(j)
                    A.add(j+1)
            else:
                if j+1 not in B:
                    d.append(j)
                    B.add(j+1)
#N/2以上の点を含む列を探して出力
if len(A)>=len(B):
    A=list(A)
    print(" ".join(map(str,A[:N//2])))
else:
    B=list(B)
    print(" ".join(map(str,B[:N//2])))
