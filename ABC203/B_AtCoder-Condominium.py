#問題文
#https://atcoder.jp/contests/abc203/tasks/abc203_b

#入力
n,k=map(int,input().split())

#各部屋の百の位の合計値
S=0
#各部屋の一の位の合計値
s=0

#Sを求める全探索
for i in range(1,n+1):
    S+=i*100*k
    
#sを求める全探索
for i in range(1,k+1):
    s+=i*n

print(S+s)
