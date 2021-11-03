import sys
input=sys.stdin.readline

# 入力(日数、目標金額)
N,S=map(int,input().split())

# dp[i日目の時点で][総額j円が可能か]　　0なら不可、1なら可能
dp=[[0]*(S+1) for _ in range(N+1)]

# 0日目0円は可能
dp[0][0]=1

# 福袋の金額管理
A=[0]*(N+1)
B=[0]*(N+1)
for i in range(1,N+1):
    a,b=map(int,input().split())
    A[i]=a
    B[i]=b
    

# 1日目から各金額に到達可能か考えていく（計算量は10^7以下）
for i in range(1,N+1):
    a=A[i]
    b=B[i]
    for j in range(S+1):
        # i-1日目にj円が可能なら、i日目にj+A[i]円とj+B[i]円が可能
        if dp[i-1][j]==1:
            if j+a<=S:
                dp[i][j+a]=1
            if j+b<=S:
                dp[i][j+b]=1

# N日目S円が不可能ならImpossibleを出力。プログラム終了
if dp[N][S]!=1:
    print("Impossible")
    sys.exit()

# 出力する答えと残りの金額
ans=""
money=S

# N日目から逆算。
for i in reversed(range(1,N+1)):
    # i日目の残額から福袋の金額を引いて、
    # ①残額が負にならない ②i-1日目の残額が可能のときに残額更新と解追加
    if money-A[i]>=0 and dp[i-1][money-A[i]]==1:
        ans="A"+ans
        money-=A[i]
    elif money-B[i]>=0 and dp[i-1][money-B[i]]==1:
        ans="B"+ans
        money-=B[i]

# 出力
print(ans)
