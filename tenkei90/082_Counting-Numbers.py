#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_cd

#入力
L,R=map(int,input().split())

#num[i]には10**iから10**(i+1)-1の和が入る
num=[45]
for i in range(2,19):
    n=10**i-1
    num.append(n*(n+1)//2-sum(num))
    
#入力が 1 xであったときの答えを計算する関数
def f(x):
    global num
    I=len(str(x)) #桁数
    
    ans=0
    #ex:x=1005なら1~999までの処理をここで行う
    for i in range(I-1):
        ans+=num[i]*(i+1)   
        
    #ex:1000~1005の処理
    ans+=(x*(x+1)//2-sum(num[0:I-1]))*I 
    
    return ans

r_ans=f(R)
l_ans=f(L)

#Lを余分に引いたので処理
A=r_ans-l_ans+len(str(L))*L

print(A%(10**9+7))
#print(r_ans,l_ans)
