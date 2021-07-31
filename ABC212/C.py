from bisect import bisect_left,bisect_right

# 入力
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()  # 並び替え

ans=10**9  # 解の設定(初期値を解の最大値より大きく設定)

A=[-1*10**9]+A+[2*10**9+1] # Aの両端に加えることで下の処理が楽に行える

"""
Bの要素をA(ソート済み)のどこに入るのか二分探索して、
その両端の値との差を抽出、この中から最小値を探した
"""
for b in B:
    index =bisect_left(A, b)  # Bの要素の挿入位置
    ans=min(ans, min(b-A[index-1], A[index]-b) )  # ans との比較
    
print(ans)
