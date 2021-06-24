#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_m

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

    #dilkstraで解ける
    
    #街 k+1 から各街へ行くときにかかる最小コスト
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
    
    #街 1 から各点へ行くときにかかる最小コスト
    D0=func(0)
    #街 N から各点へ行くときにかかる最小コスト
    D1=func(N-1)
    
    #街 1 から街 i+1 を経由して街 N まで移動するときにかかるコスト
    #　＝（街 1 から街 i+1へ行くときにかかる最小コスト）
    #     ＋（街 N から街 i+1へ行くときにかかる最小コスト）
    for i in range(N):
        print(D0[i]+D1[i])

main()
