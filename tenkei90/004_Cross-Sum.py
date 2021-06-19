#https://atcoder.jp/contests/typical90/tasks/typical90_d
#行と列の和をそれぞれ事前に計算して各i,jに対してその和-A[i][j]を表示した

H,W=map(int,input().split())
A=[]
gyou=[0 for _ in range(H)]
retu=[0 for _ in range(W)]
for i in range(H):
    A.append(list(map(int,input().split())))
    gyou[i]+=sum(A[i])
    retu=[(x+y) for (x,y) in zip(retu,A[i])]

for i in range(H):
    B=[]
    for j in range(W):
        B.append(gyou[i]+retu[j])
    B=[(x-y) for (x,y) in zip(B,A[i])]
    print(" ".join(map(str,B)))
