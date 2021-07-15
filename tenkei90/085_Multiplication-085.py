#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_cg

#入力
K=int(input())

#解答
cnt=0

# aの最大値
x=int(K**(1/3)) # 整数が丸まって想定より1小さくなることがある

for a in range(1,x+2): 
    if K%a==0:
        K2=K//a
        
        # bの最大値
        y=int(K2**(1/2)) #これは丸まらない
        # この範囲なら自動的にa<=b<=cになる
        for b in range(a,y+1):
            if K2%b==0:
                cnt+=1
print(cnt)
