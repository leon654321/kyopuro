from math import sqrt, gcd, factorial

#入力
p=int(input())

#　N!　円のリストを作成
C=[factorial(i) for i in range(1,11)]
#print(C)

#答え
ans=0

# 10! 円からできる限り払い続ける
for i in reversed(C):
    ans+=p//i
    p%=i
    #print(ans)
    #print(p)
    
print(ans)
