from bisect import bisect_left

"""
最長部分増加列を考えればよい
"""
# 入力　数列Aの長さNとA
N=int(input())
A=list(map(int,input().split()))

# 部分増加列の計算
def func(a):
    #部分増加列
    now=[-1]
    
    # jun[i]にはi番目まで考慮した時の最長部分増加列の長さが入る
    jun=[0]*N
    
    # 前方から列を調べる
    for i in range(N):
        # j:a[i]が増加列に入る位置
        j=bisect_left(now,a[i])
        
        # a[i]を考慮した時の増加列の長さを記録
        jun[i]=j
        
        # もし増加列の最右端に来るなら追加違うなら書き換え
        if j==len(now):
            now.append(a[i])
        else:
            now[j]=a[i]
    return jun

# 昇順
x=func(A)
# Aをひっくり返して計算
y=func(A[::-1])

# 昇順降順を考慮して題意の最大値を調べる
ans=0
for i in range(N):
    z=x[i]+y[N-1-i]-1
    ans=max(ans,z)

#出力
print(ans)
