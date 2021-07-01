import sys
sys.setrecursionlimit((10 ** 9))  # 変更
from functools import lru_cache

#最大公約数の関数
@lru_cache(maxsize=None)
def eucrid(x,y):
    if y>x:
        x,y=y,x
    z=x%y
    if z==0:
        return y
    else:
        return eucrid(y,z)
     
#入力
a,b,c=map(int,input().split())

#a,b,cの最大公約数
m=eucrid(a,b)
m=eucrid(m,c)

#ケーキを切る回数
ans=(a//m-1)+(b//m-1)+(c//m-1)
print(ans)
