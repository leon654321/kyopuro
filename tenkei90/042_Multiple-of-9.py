import sys
K=int(input())


# 9の倍数は必ず各桁の和が9の倍数になります
if K%9!=0:
    print(0)
    sys.exit()

# dp[i]には各桁の和がiになる数字の数が入る
dp=[0]*(K+1)


"""
dp[i]は以下の通り構成される
先頭が1 + dp[i-1]
先頭が2 + dp[i-2]
    :
    :
    :
先頭が9 + dp[i-9]
"""
# まずdp[9]まで作成（最後の+1は一桁のとき用）
for i in range(1,10):
    dp[i]=sum(dp[:i])+1

# dp[10]以降を作成
for i in range(10,K+1):
    for j in range(1,10):
        dp[i]+=dp[i-j]
        dp[i]%=(10**9+7)

print(dp[K]%(10**9+7))
