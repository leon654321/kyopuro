#問題文
#https://atcoder.jp/contests/abc206/tasks/abc206_b

N=int(input())

for i in range(10**5):
    #合計金額がNを超えたらfor文から抜ける
    if N<=(i*(i+1)//2):
        break
#breakしたときのiがそのまま答えとなる
print(i)
