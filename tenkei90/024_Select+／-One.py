#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_x

#入力
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

#AとBの差の絶対値
C=[abs(A[i]-B[i]) for i in range(N)]

#差の絶対値の和
s=sum(C)


if K>=s and(K-s)%2==0:
    print("Yes")
#たとえK>=sでも差が奇数なら0にできない
else:
    print("No")
