from itertools import permutations, combinations, product, combinations_with_replacement, groupby, accumulate

# グリッド入力
H,W=map(int,input().split())
P=[list(map(int,input().split())) for _ in range(H)]

# ans[i]には数字iで構成される部分グリッドの大きさの最大値が入る
ans=[0]*(H*W+1)

"""
基本的には全探索。まず行を選ぶ。これはH<=8より最大計算量は
8C1 + ... +8C8 = 255

次に各列を見ていく。ある列に書かれている数字が同じでそれが i だったら
num[i]に行の数(その数字のとる面積)だけ＋する

最後にnumを使ってansを更新

最終的な計算量はO(10^7)
"""

ls=[i for i in range(H)]

# 行を選ぶ数:(H)Combination(i)
for i in range(1,H+1):
    # nCiの総当たり
    for j in combinations(ls,i):
        
        # iとjの制約下でのans
        ij_ans=[0]*(H*W+1)
        
        # 各列についてみていく
        for k in range(W):
            # 選んだ中で最も上の行、k列目に書いてある数字
            z=P[j[0]][k]
            
            # ある列がすべて同じ数字でできているか判定
            T=True
            
            # ある列に違う数字が混じっていたらT=False
            for l in range(1,i):
                if P[j[l]][k]!=z:
                    T=False
                    break
            
            # ある列がすべて同じ数字だったら+iする
            if T:
                ij_ans[z]+=i
                
        # ansを更新
        for m in range(1,H*W+1):
            if ans[m]<ij_ans[m]:
                ans[m]=ij_ans[m]
        
        
# 出力
print(max(ans))
