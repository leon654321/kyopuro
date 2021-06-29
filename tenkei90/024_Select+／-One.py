#
#

#
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[abs(A[i]-B[i]) for i in range(N)]
s=sum(C)

if K>=s and(K-s)%2==0:
    print("Yes")
else:
    print("No")
