#問題文
#https://atcoder.jp/contests/abc206/tasks/abc206_c

from collections import defaultdict, Counter, deque
N=int(input())
A=list(map(int,input().split()))
B=defaultdict(int)

#A[i]の値をB[A[i]]として記録。A[i]=A[j]ならB[A[i]]=2になる
for i in A:
    B[i]+=1

cnt=0
for i in range(N):
    B[A[i]]-=1
    #自分より後ろにある要素の数-後ろにある自分と同じ値の数
    cnt+=N-1-i-B[A[i]]
print(cnt)
