import sys

from collections import deque

N=int(input())
A=set([])
B=set([])
al=set([])
d=deque([])
G=[[] for i in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

d.append(0)
al.add(0)
A.add(1)
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

if len(A)>=len(B):
    A=list(A)
    print(" ".join(map(str,A[:N//2])))
else:
    B=list(B)
    print(" ".join(map(str,B[:N//2])))
