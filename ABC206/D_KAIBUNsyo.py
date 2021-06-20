#問題文
#https://atcoder.jp/contests/abc206/tasks/abc206_d

"""
N=5の場合、i=3は無視してi=1,2,4,5だけに注目すればよく、これを(1,5),(2,4)のようなペアで管理すれば、どんなに多くとも2回つまりN//2回で済むと分かる
以下Z=N//2がどのようなときに-1されるのか、つまり回文にするための回数が1回少なくなるのかを見る

ex1:
A=1,2,3,4,5,1のとき。つまり(1,1),(2,5),(3,4)のとき。(1,1)はすでに回文なのでこの分だけ-1される

ex2:
A=1,2,4,1,3,4のとき。つまり、(1,4),(2,3),(4,1)のとき。これは(1,4),(2,3)と同じ処理で済むので-1される

ex3:
A=1,2,3,1,3,2のとき。つまり、(1,2),(2,3),(3,1)のとき。
少しわかりづらいが、1⇒2⇒3⇒1のようなループができているので普通の場合より1回だけ少なく済む

以上のex1~3はすべてunion-findで管理すれば楽になる
"""

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N=int(input())
A=list(map(int,input().split()))

Z=N//2 #答えの最大値
uf=UnionFind(2*10**5+1)
        
for i in range(N//2):
    if uf.find(A[i])==uf.find(A[N-1-i]):
        Z-=1
    else:
        uf.union(A[i],A[N-i-1])

print(Z)
