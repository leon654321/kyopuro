#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_cf

#入力
N=int(input())
S=input()

num=[0]  #どのindexで"o"と"×"が切り替わった格納するリスト
a=S[0]   #切り替わりに反応する変数
    
for i in range(1,len(S)):
    #切り替わったら位置を格納
    if S[i]!=a:
        num.append(i)
        a=S[i]  #aを修正

num.append(len(S))

ans=0  #答え

for i in range(len(num)-2):
    # S[num[i]] から S[num[i+1]-1] は同じ文字(例えば"o")
    # S[num[i+1]] から始まる S[num[-1]] までの文字列は必ず上記と
    #異なる文字("×")を含んでいる
    ans+=(num[i+1]-num[i])*(num[-1]-num[i+1])

print(ans)
