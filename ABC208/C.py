from bisect import bisect_left,bisect_right

#入力
N,K=map(int,input().split())
A=list(map(int,input().split()))

#Aを昇順にしたリスト作成
B=sorted(A)

#全員に均等に配られる分
ans=K//N
#全員に配れず余った分
z=K%N

# index はA[i]が全体で下から何番目に位置するか計算している。
#このとき普通にB.index(A[i])とやるとN^2でTLEになる。それを回避するために二分探索を行った。
for i in range(N):
    index=bisect_left(B,A[i])
    #print(index)
    if index<=z-1:
        print(ans+1)
    else:
        print(ans)
