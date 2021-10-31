from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint
from copy import deepcopy
from decimal import *

def I(): return input()
def II(): return int(input())
def MI(): return map(int,input().split())
def LMI(): return list(map(int,input().split()))
def LLMI(number): return [list(map(int,input().spkit())) for _ in range(number)]

#sys.setrecursionlimit((10 ** 9))  # 変更
input = sys.stdin.readline

N=II()

"""
偏角のようなものを用意して考えればただのスケジューリング問題になる
今回は偏角ではなく傾きを用いた。つまり
右端と左端のタプルで構成されたリストを右端の昇順でソート

残っているものの中で最小の右端のペアから調べていって、
今の右端より大きな左端を持つペアがいれば cnt+=1、
そのペアの右端を現在の最大値として次のループへ移る
"""

G=[]
for _ in range(N):
    x,y=map(Decimal,input().split())
    m=(y-1)/x                         # 傾き最小(左端に相当)
    M=y/(x-1) if x!=1 else 10**15     # 傾き最大(右端に相当)
    G+=[(M,m)]

# Mに関して昇順ソート(Mが同じならmでソート)    
G.sort()

ang=0 # 傾き
cnt=0 # 答え

# 最小の右端から探索
for i in range(N):
    M,m=G[i]
    # 現在の右端より大きな左端を見つけた場合
    if ang<=m:
        cnt+=1
        ang=M

# 出力
print(cnt)
