import sys
input=sys.stdin.readline


# 入力（総段数、一度に登れる段数）
N,L=map(int,input().split())

# i段目まで登る通り数。L-1 段目までは1通りしかないので初期値は1にしている
dp=[1]*(N+1)

# L段目以降の移動方法
for i in range(L,N+1):
    # i段目に行くには ①:i-1段目から ②:i-L段目から　のいずれか
    dp[i]=dp[i-1]+dp[i-L]
    dp[i]%=(10**9+7)
    
# 答えと出力
ans=dp[N]
print(ans)
