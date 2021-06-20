#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_af

#制約が小さいため全探索でも間に合う。permutationsを使う
import itertools

N = int(input())
ls=[list(map(int,input().split())) for _ in range(N)]

#仲の悪い人同士をTrueにして管理
M=int(input())
Ban=[[False]*N for _ in range(N)]
for i in range(M):
    x,y=map(int,input().split())
    Ban[x-1][y-1],Ban[y-1][x-1]=True,True

ans=10001
for p in itertools.permutations(range(N)):
    #仲が悪いかは気にせずとりあえずゴールタイム計算
    time=0
    for i in range(N):
        time+=ls[p[i]][i]
    
    #禁止された組み合わせがないか検索
    flag=True
    for i in range(N-1):
        if Ban[p[i]][p[i+1]]:
            flag=False
            break
            
    #禁止された組み合わせがないなら今までのtimeとansを比較
    if flag:
        ans=min(ans,time)
    
if ans==10001:
    print(-1)
else:
    print(ans)
