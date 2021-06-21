#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_j

#累計和的な解き方だがこのころは競プロ初心者のため作りがガタガタ

import sys
myinput=input#sys.stdin.readline
 
def func(n,cl,c_all):
    s1=0
    s2=0
    for i in range(1,n+1):
        c,p=map(int,myinput().split())
        s1+=p
        cl[i]=s1 #全生徒の累計和
        if c==1:
            s2+=p
        c_all[i]=s2    #クラス1の生徒の番号iまでの累計和
        
def func2(q,cc_all,cc):
    for _ in range(q):
        L,R=map(int,myinput().split())
        c1=cc_all[R]-cc_all[L-1] #クラス1の生徒の番号iまでの累計和から算出
        c2=cc[R]-cc[L-1]-c1 #LからRまでの全生徒の累計和からc1を引く
        print(c1,c2)        

N=int(myinput())
C=[0]*(N+1)
C_ALL=[0]*(N+1)
func(N,C,C_ALL)
Q=int(myinput())
func2(Q,C_ALL,C)
