from collections import defaultdict, Counter, deque

#入力
N,Q=map(int,input().split())
G=[[]for _ in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

    
#根から何回移動すればたどり着くか保存する
A=[0 for _ in range(N)]

#根を決める
st=0
for i in range(N):
    if len(G[i])==1:
        st=i
        break

#BFSで根から探索を始めてAの値を決めていく
d=deque([st])
al=set([st])
turn=0
while d:
    print(d)
    turn+=1
    for _ in range(len(d)):
        q=d.popleft()
        for i in range(len(G[q])):
            nex=G[q][i]
            if nex in al:
                continue
            d.append(nex)
            al.add(nex)
            A[nex]=turn

#クエリ処理
for _ in range(Q):
    #入力
    c,d=map(int,input().split())
    
    #根からの距離の差し引きを考えれば偶奇は同じになる
    ans=abs(A[d-1]-A[c-1])
    if ans%2==0:
        print("Town")
    else:
        print("Road")
