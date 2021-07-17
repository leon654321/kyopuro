#入力
n=int(input())
A=list(map(int,input().split()))

# 累積和
B=[0]*n
B[0]=A[0]
for i in range(1,n):
    B[i]=A[i]+B[i-1]

#ピラミッド的なリスト（B[4]=1*A[4]+2*A[3]+3*A[2]+4*A[1]+5*A[0] ）
C=[0]*n
C[0]=B[0]
for i in range(1,n):
    C[i]=C[i-1]+B[i]

M=0
for k in range(n):
    M=max(A[k],M)
    print(C[k]+M*(k+1))
