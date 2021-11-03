# 入力（さいころの数）
n=int(input())

"""
N=1のとき、答えは各面の和になる
N=2のとき、答えは(さいころ1の総和)×(さいころ2の総和)になる
以上を踏まえればN=Zのとき答えは以下の通り
(さいころ1の総和)×...×(さいころZの総和)
"""

ans=1
for i in range(n):
    #答えにi番目のさいころの総和をかける
    ans*=sum(map(int,input().split()))
    ans%=(10**9+7)
    
# 出力
print(ans)