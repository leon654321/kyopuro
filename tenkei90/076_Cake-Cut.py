#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_bx

import sys

#入力
N=int(input())
A=list(map(int,input().split()))

#ケーキの10分の1
S=sum(A)//10

#10分の1に切れなかったらNo
if sum(A)%10 !=0:
    print("No")
    sys.exit()

"""
あるケーキを取ってSより小さかったら次のケーキを取る(ans+=A[i])
もしSより大きかったら今持ってる中で一番最初に取ったケーキを置く(ans-=A[dis])
これを繰り返してN番目のケーキを置いたら探索終了
"""    
  
ans=0 #連続したケーキの大きさ
dis=0 #捨てるケーキの番号
i=0   #とるケーキの番号

#N番目のケーキを置いたら探索終了
while dis!=N:
    
    #ケーキをとる
    ans+=A[i]
    
    #10分の1になったら探索終了（sys.exit()）
    if ans==S:
        print("Yes")
        sys.exit()
    
    #Sより大きかったら今持ってる中で一番最初に取ったケーキを置く
    if ans>S:
        ans-=A[dis]
        dis+=1
        
    i+=1
    
    if i==N:
        i=0
        
#10分の1ににできなかった場合
print("No")
