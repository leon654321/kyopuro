from collections import deque,defaultdict
import sys
input=sys.stdin.readline

def main():
    N,M=map(int,input().split())
    G=[[] for _ in range(N)]
    for _ in range(M):
        a,b,c=map(int,input().split())
        G[a-1].append((b-1,c))
        G[b-1].append((a-1,c))


    def func(k):
        d=defaultdict(lambda:10**9+1)
        d[k]=0
        q=deque([(k,d[k])]) #エッジ番号,ここまでのコスト
        qpl=q.popleft
        qapp=q.append

        while q:
            num,dist=qpl()
            for nxt,cost in G[num]:
                new_dist=dist+cost
                if d[nxt]<=new_dist:
                    continue
                d[nxt]=new_dist
                qapp((nxt,new_dist))

        return d

    D0=func(0)
    D1=func(N-1)

    for i in range(N):
        print(D0[i]+D1[i])

main()
