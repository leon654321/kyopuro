import sys
input=sys.stdin.readline

# 入力（整数の数、法、あまり）、整数列
n,p,q=map(int,input().split())
A=list(map(int,input().split()))


"""
全探索を行う
n<=100で制限5secなので最大でも計算量は 8*10^7程度。楽々間に合う
"""

# 答え
cnt=0
for i in range(n-4):
    I=A[i]
    for j in range(i+1,n-3):
        J=A[j]
        for x in range(j+1,n-2):
            X=A[x]
            for y in range(x+1,n-1):
                Y=A[y]
                for z in range(y+1,n):
                    Z=A[z]
                    # オーバーフローを防ぐため、%pを挟んでいる
                    if (I*J%p*X%p*Y%p*Z)%p == q:
                        cnt+=1
# 出力
print(cnt)
