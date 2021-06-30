#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_bw

import sys

#入力
N=int(input())
n=N

#素数で割った回数
cnt=0

#素数で試しわり
for i in range(2,max(int(N**(1/2))+1,3)):
    if N%i==0:
        cnt+=1
        N//=i
        
        while N%i==0:
            cnt+=1
            N//=i


#上のループの範囲外の素数を因数に持っていたら+1
if N!=1 and cnt>0:
    cnt+=1
    
    
#print(prime)
#print(len(A))

#入力が素数の場合(N=2は上のループで加算されてしまう)
if cnt==0 or n==2:
    print(0)
    sys.exit()

#cnt-1を2進数表記に直した時の桁数
ans=len(bin(cnt-1))-2

print(ans)
