#037 - Don't Leave the Spice（★5）
#####segfunc#####
def segfunc(x, y):
    return max(x,y)
#################

#####ide_ele#####
ide_ele =-1
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

# 入力
W,N=map(int,input().split())
G=[list(map(int,input().split())) for _ in range(N)]

# セグメント木生成
st=SegTree([0]*(W+1) ,segfunc,ide_ele)

"""
セグメント木には価値とある範囲の最大値を代入していく

"""

#　各香辛料について精査していく
for i in range(1,N+1):
    L=G[i-1][0]
    R=G[i-1][1]
    cost=G[i-1][2]
    
    #一時的に価値を代入していく
    dp=[0]*(W+1)
    
    for j in range(1,W+1):
        #　合計j mg の香辛料についてそのR mg, L mg　少ない値の範囲で最大値を求める
        before=st.query(max(0,j-R),max(0,j-L)+1)
        
        # 価値0からの遷移は何も選んでない状態からだけ、j-L mgが0 mg より大きな場合だけ進めていく
        if ( before == 0 and max(0,j-R)!=0 ) or j-L<0:
            continue
        
        #　i番目の香辛料を選んだ場合の遷移結果について代入していく
        dp[j]=before + cost
        
    # i番目の香辛料を選んだ場合、選ばなかった場合について比較して木に代入していく
    for j in range(W+1):
        st.update(j, max( st.query(j,j+1) , dp[j] ) )
        
        
        
#ちょうど W mg にできるかどうか
ans=st.query(W,W+1)

#ちょうど W mg にできない
if ans==0:
    print(-1)
    
#ちょうど W mg にできる
else :
    print(ans)

