#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_h

#入力
N=int(input())
S=input()

#各文字定義
a,t,c,o,d,e,r=0,0,0,0,0,0,0

#Sを逆順で見ていってある文字（例えば"E"）があればそこから後ろに"R"
#が何通り選べるかを蓄積していく。これを以後"D", "O",,,"A"と続けていけば
#for文が終わった時点でのa(AtCoderのイニシャル)の値が解となる
for x in reversed(S):
    if x=="r":
        r+=1
    elif x=="e":
        e+=r
    elif x=="d":
        d+=e
    elif x=="o":
        o+=d
    elif x=="c":
        c+=o
    elif x=="t":
        t+=c
    elif x=="a":
        a+=t

print(a%(10**9+7))
