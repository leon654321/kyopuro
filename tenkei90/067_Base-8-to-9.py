#入力(nは文字列として入力)
N,K=input().split()
K=int(K)


def f(n):
    # 10進法に変換
    n=str(int(n,base=8))
    
    # 9進法であらわすとi桁になる
    i=0
    while 9**i<=s:
        i+=1
    
    # 9進法に変換
    ans=""
    for j in reversed(range(i)):
        A=str(s//(9**j))
        if A=="8":
            ans+="5"
        else:
            ans+=A
        s%=(9**j)
        
    # 入力が0のときの処理
    if ans=="":
        ans="0"
    return ans

# K回操作を行う
for _ in range(K):
    N=f(N)

# 出力    
print(N)
