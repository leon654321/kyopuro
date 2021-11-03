import sys
input=sys.stdin.readline

# 入力（列の数、色の種類）
N,K=map(int,input().split())

# N<=2またはK<=2の場合の処理
if N==1:
    print(K)
elif N==2:
    if K==1:
        print(0)
    else:
        print(K*(K-1)%(10**9+7))
elif K<=2:
    print(0)
    
# NとKがある程度大きい時の処理
# 最初の二種類を選べば残りのN-2列はK-2種類から選び続ければよい
else:
    ans=K*(K-1)%(10**9+7)
    z=pow(K-2,N-2,10**9+7)
    
    print(ans*z%(10**9+7))
