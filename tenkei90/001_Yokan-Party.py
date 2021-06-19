#1 Yokan Party（★4）AC
"""
左右の長さが L [cm] のようかんがあります。 
N 個の切れ目が付けられており、左から i 番目の切れ目は左から 
Ai [cm] の位置にあります。
あなたは N 個の切れ目のうち K 個を選び、ようかんを 
K+1 個のピースに分割したいです。そこで、以下の値を スコア とします。
K+1 個のピースのうち、最も短いものの長さ（cm 単位）
スコアが最大となるように分割する場合に得られるスコアを求めてください。

方針
ある値のXよりおおきくようかんを切り分けられるか考えて、Xを二分探索した
"""


import sys
sys.setrecursionlimit((10 ** 9))  # 変更
from functools import lru_cache
myinput=input#sys.stdin.readline

@lru_cache(maxsize=None)
def cut(n,k,l,r,m):
    global piecies,L
    if l==m:
        if r!=L//(k+1):
            print(l)
            return
        else:
            print(r)
            return
    cnt=0
    i=0
    P=[0]
    #print(l,r,m)
    for j in range(n+1):
        if P[i]<m and i<=k:
            P[i]+=piecies[j]
        elif P[i]>=m and i<k:
            i+=1
            P.append(piecies[j])
        else:
            P[-1]+=piecies[j]
    if len(P)==k+1 and P[-1]>=m:
        l=m
        m=(l+r)//2
        return cut(n,k,l,r,m)
    else:
        r=m
        m=(l+r)//2
        return cut(n,k,l,r,m)

N,L=map(int,myinput().split())
K=int(myinput())

youkan=[0]+list(map(int,myinput().split()))+[L]
piecies=[youkan[i]-youkan[i-1] for i in range(1,N+2)]
left=min( piecies )
right=L//(K+1)
mid=(left+right)//2
#print(left,right,mid)
cut(N,K,left,right,mid)
