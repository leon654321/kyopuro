#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_h

N=int(input())
S=input()

#少しでも速度を早くしたかったので.appendの呼び出しがなくなるようにした
a=[]
aappend=a.append
t=[]
tappend=t.append
c=[]
cappend=c.append
o=[]
oappend=o.append
d=[]
dappend=d.append
e=[]
eappend=e.append
r=[]
rappend=r.append

#Sを逆順で見ていってある文字（例えば"E"）があればそこから後ろに"R"
#が何通り選べるかを蓄積していく。これを以後"D", "O",,,"A"と続けていけば
#for文が終わった時点でのリストaの合計が解となる
for x in reversed(S):
    if x=="r":
        rappend(1)
    elif x=="e":
        eappend(sum(r))
    elif x=="d":
        dappend(sum(e))
    elif x=="o":
        oappend(sum(d))
    elif x=="c":
        cappend(sum(o))
    elif x=="t":
        tappend(sum(c))
    elif x=="a":
        aappend(sum(t))

print(sum(a)%(10**9+7))
