#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_p

import sys
myinput=input#sys.stdin.readline

#入力
N=int(myinput())
ls=list(map(int,myinput().split()))

#A,B,C円を昇順並び替え
ls=sorted(ls,reverse=True)

a,b,c=ls[0],ls[1],ls[2]
num=9999

#A円硬貨の最大数
N1=N//a

for i in range(N1+1):
    
    #A円硬貨i枚のときのB円硬貨の最大数
    N2=(N-a*i)//b
    
    #9999とN2を比較して小さい方を上限値として探索
    for j in reversed(range(min(10000-i,N2+1))):
        
        #A円硬貨がi枚、B円硬貨がｊ枚のときのＣ円硬貨の数
        N3=(N-a*i-b*j)//c
        
        #効果がすべてでＮ枚で、かつ9999枚以下
        if a*i+b*j+c*N3==N and num>(i+j+N3):
            num=i+j+N3
            break
        #この条件に到達したら以降はかならず9999よりおおくなるのでbreak
        elif i+j+N3>num :
            break


print(num)   
