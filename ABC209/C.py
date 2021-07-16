from bisect import bisect_left,bisect_right
import sys
input=sys.stdin.readline

#入力
N=int(input())
B=list(map(int,input().split()))

#Bを昇順並び替え(B.sort()で間に合うらしい…ちなみにsorted, bisect_leftでは間に合わない)
C=[]
for i in range(N):
    index=bisect_right(C,B[i])
    C.insert(index, B[i])
    
#小さい順に使う数を決めていく(数を使い果たしてしまったら0になる)
ans=C[0]
for i in range(1,N):
    ans*=(C[i]-i)
    ans%=(10**9+7)
    
print(ans)
