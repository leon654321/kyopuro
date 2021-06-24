#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_n

import sys
myinput=sys.stdin.readline

#入力
N=int(myinput())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

#学校、家の位置を昇順に並び替え
A=sorted(A)
B=sorted(B)

"""
数直線で考えて単純に一番左に住んでいる生徒は一番左の学校に通えば不便さが最小になる

       (学校1)　　　　　　(学校2)

(家1)　　　　    (家2)

例えば上記のような学校、家の配置の場合、
A:家1から学校1、家2から学校2
B:家1から学校2、家2から学校1

上記の二通りがあるがBはAに比べて、(家2から学校1の距離)×2だけ損していることがわかる
"""
C=[abs(A[i]-B[i]) for i in range(N)]

#不便さの合計
print(sum(C))
