from collections import defaultdict, Counter, deque
import sys
sys.setrecursionlimit((10 ** 9))  # 変更

# 入力
N,Q=map(int,input().split())

# d[i]はiの後ろ（または前）にくる車両の番号を管理
# 連結していないならd[i]=0
d_back=defaultdict(int)
d_front=defaultdict(int)

# 最初は全部分離している
for i in range(1,N+1):
    d_back[i]=0
    d_front[i]=0

# 後部の車両を追う処理
def kid(j):
    global ans
    ans.append(j)
    ans[0]+=1
    if d_back[j]!=0:
        kid(d_back[j])
        
# 前方の車両を追う処理
def par(k):
    global P
    if d_front[k]!=0:
        par(d_front[k])
    else :
        P=k
        
    

for _ in range(Q):
    # クエリ入力
    ls=list(map(int,input().split()))
    
    # クエリの長さごとに変数指定
    if len(ls)==3:
        num,x,y = ls[0], ls[1], ls[2] 
    else:
        num,x = ls[0], ls[1]
    
    # 連結処理
    if num==1:
        d_back[x]=y
        d_front[y]=x
    # 分離処理
    elif num==2:
        d_back[x]=0
        d_front[y]=0
    # 先頭車両を求めてから後ろの車両を追っていく
    elif num==3:
        # 出力列 ans[0]は車両の個数
        ans=[0]
        
        # 先頭車両を求める
        P=0
        par(x)
        
        # 最後尾の車両まで探索
        kid(P)
        
        # 出力
        print(*ans)
