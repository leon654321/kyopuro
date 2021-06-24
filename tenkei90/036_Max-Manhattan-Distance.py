#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_aj

import sys
input=input#sys.stdin.readline
N,Q=map(int,input().split())
X=[0]*N
Y=[0]*N
for i in range(N):
    x,y=map(int,input().split())
    #これでマンハッタン距離＝max(X[i],Y[i])になる
    X[i]=x-y
    Y[i]=x+y

#マンハッタン距離が最大となる候補は上下左右端の4点のみ
Xm,XM=min(X),max(X)
Ym,YM=min(Y),max(Y)

def main():
    for i in range(Q):
        num=int(input())-1
        #上下左右端と比較して最大（＝マンハッタン距離）の値をprint
        print(max(max(XM-X[num],X[num]-Xm),max(YM-Y[num],Y[num]-Ym)))
main()
