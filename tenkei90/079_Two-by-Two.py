#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_ca

import sys

#入力
H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]
B=[list(map(int,input().split())) for _ in range(H)]

cnt=0 #操作回数

#グラフの最上段はi=0のときしか操作できず最左列はj=0の下でしか操作できないため
#逆に言えば左上からBと同じなるように処理すればそれが必要最低回数である
for i in range(H-1):
    for j in range(W-1):
        if A[i][j]!=B[i][j]:
            K=(B[i][j]-A[i][j]) #AとBの差
            
            #問題文にある通りの処理
            A[i][j]+=K
            A[i+1][j]+=K
            A[i][j+1]+=K
            A[i+1][j+1]+=K
            
            cnt+=abs(K) #操作回数を増やす

#AとBが同じかチェック
for i in range(H):
    for j in range(W):
        if A[i][j]!=B[i][j]:
            #1つでも異なればその時点で終了
            print("No")
            sys.exit()

print("Yes")
print(cnt)
