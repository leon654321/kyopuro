#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_t

#入力
a,b,c=map(int,input().split())

#2の指数に乗せれば2^(log2a)=a, 2^(log2c^b)=c^bなのでそれを比較すればよい
if a<c**b:
    print("Yes")
else:
    print("No")
