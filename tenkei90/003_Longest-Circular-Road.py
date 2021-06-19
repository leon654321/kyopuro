from collections import deque

N=int(input())
al=set([])
d=deque([])
G=[[] for i in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

d.append(0)
al.add(0)
while d:
    L=len(d)
    for i in range(L):
        D=d.popleft()
        for j in G[D]:
            if j not in al:
                al.add(j)
                d.append(j)
#print(D)
d.append(D)
al=set([D])
cnt=0
while d:
    cnt+=1
    #print(d)
    L=len(d)
    for i in range(L):
        D=d.popleft()
        for j in G[D]:
            if j not in al:
                al.add(j)
                d.append(j)            
print(cnt)
