from collections import deque

#入力
N,K=map(int,input().split())
A=list(map(int,input().split()))

#答え
ans=0

#現在見ている部分列
Q=deque([])

# Qに含まれる各数字についてその出現回数を記録
d={}

# Qに含まれる数字の種類
kind=0

for i in range(N):
    a=A[i]
    
    # aを部分列に追加
    Q.append(a)
    
    ### aが既にQに含まれていたか判定
    # aがQに含まれていなかったら辞書を作成、種類を追加
    if a not in d:
        d[a]=1
        kind+=1
    # aがQにいたなら辞書に+1する
    else:
        d[a]+=1
        
    ### Qに K+1 種類以上の数字がいる場合の処理    
    while kind>K:
        
        # Qの左端を削除
        q=Q.popleft()
        
        # もしqと同じ数字がQ内にないなら辞書を削除、種類を-1する、while文脱出
        if d[q]==1:
            d.pop(q)
            kind-=1
        # まだQに同じ数字があるなら辞書から-1するだけ、while文継続
        else:
            d[q]-=1
        
    # 解の更新
    ans=max(ans,len(Q))

print(ans)
