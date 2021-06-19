import sys
myinput=input#sys.stdin.readline

N=int(myinput())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A=sorted(A)
B=sorted(B)
C=[abs(A[i]-B[i]) for i in range(N)]
print(sum(C))
