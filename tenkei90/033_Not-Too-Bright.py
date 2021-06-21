#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_ag

"""

#-#-#   
-----
#-#-#

という感じでやると最大
ただし例外はH or W=1のときで

#####　

は不適切ではない（2*2の領域に完全に含まれていないため）
"""

h,w=map(int,input().split())
if h==1 or w==1:
    print(h*w)
else:
    h=(h+1)//2
    w=(w+1)//2
    print(h*w)

