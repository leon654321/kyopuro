#入力
N,M=map(int,input().split())
B=[list(map(int,input().split()))for _ in range(N)]

# cntとの比較でB[i][j]が条件に適しているか確認
# 条件と会わなければ flag=False
cnt=B[0][0]-(7)+M-1
flag=True

for i in range(N):
    cnt+=7
    cnt-=M
    for j in range(M):
        cnt+=1
        #print(cnt,B[i][j])
        
        # B[i][j]が連続的でなかったり列の変化時に不自然に飛んでたりする場合
        if cnt!=B[i][j]:
            flag=False
        # j=0以外で7の倍数が表れるのも不適
        if j!=M-1 and B[i][j]%7==0:
            flag==False

# 出力
if flag :
    print("Yes")
else:
    print("No")
