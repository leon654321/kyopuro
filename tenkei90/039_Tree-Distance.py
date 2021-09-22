import sys
sys.setrecursionlimit((10 ** 9))  # 再帰回数変更

#入力
N=int(input())
G=[[] for _ in range(N)]

#木作成
for _ in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

ans=0　#解答
al=[False]*N  #通過済みかどうか
kid=[1]*N  #木構造で自分の下にいくついるか（自分含む）

#深さ優先探索
def dfs(cur):
    global ans
    
    al[cur]=True  #通過しました
    
    #自分の子を探索する
    for nxt in G[cur]:
        if not al[nxt]:
            dfs(nxt)
            kid[cur]+=kid[nxt]  #子供の数を自分に足す
    
    
    ans+=kid[cur]*(N-kid[cur])  # 自分を通る回数だけansに足す
    
dfs(0) #0を親にして探索

#出力
print(ans)
