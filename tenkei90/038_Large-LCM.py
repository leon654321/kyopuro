#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_al

import sys
sys.setrecursionlimit((10 ** 9))  # 変更
from functools import lru_cache
@lru_cache(maxsize=None)

#ユークリッドの互除法で最大公約数計算
def eucrid(x,y):
    if y>x:
        x,y=y,x
    z=x%y
    if z==0:
        return y
    else:
        return eucrid(y,z)

A,B=map(int,input().split())
a,b=A,B
C=eucrid(a,b)

#最小公倍数＝A*B*(AとBの最大公約数)
ans=A*B//C

if ans>10**18:
    print("Large")
else:
    print(ans)
