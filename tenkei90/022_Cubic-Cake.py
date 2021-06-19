import sys
sys.setrecursionlimit((10 ** 9))  # 変更
from functools import lru_cache

@lru_cache(maxsize=None)
def eucrid(x,y):
    if y>x:
        x,y=y,x
    z=x%y
    if z==0:
        return y
    else:
        return eucrid(y,z)
        
a,b,c=map(int,input().split())
m=eucrid(a,b)
m=eucrid(m,c)

ans=(a//m-1)+(b//m-1)+(c//m-1)
print(ans)
