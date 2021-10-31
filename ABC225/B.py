from collections import defaultdict, Counter, deque

#入力
N=int(input())

# スターならすべてのノードとつながるエッジが存在
#  ＝あるエッジの出現回数がN-1

# 出現回数管理
cnt=defaultdict(int)

for i in range(N):
    a,b=map(int,input().split())
    cnt[a]+=1
    cnt[b]+=1

# defaultdictの最大値を管理
num=0
for i in cnt:
    num=max(num,cnt[i])
    
# 出力
if num==N-1:
    print("Yes")
else:
    print("No")
