#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_aa

import sys
myinput=sys.stdin.readline

N=int(myinput())

#既にいるユーザー名管理
ls=set([])

for i in range(1,N+1):
    x=myinput()
    
    #すでにユーザー名が登録されているか判定
    if x in ls:
        continue
    else:
        ls.add(x)
        print(i)
