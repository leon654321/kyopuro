#問題文
#https://atcoder.jp/contests/abc206/tasks/abc206_a

N=int(input())

#1.08をかけた後に切り捨てを行っています
N=(N*1.08)//1

#条件合わせ
if N<206:
    print("Yay!")
elif N==206:
    print("so-so")
else:
    print(":(")
