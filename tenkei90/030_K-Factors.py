#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_ad

N,K=map(int,input().split())

#sosu[i]が0なら（iが素数なら）、iの倍数をすべて＋1する
#例えばi=6ならi=2, 3でそれぞれ+1されるのでsosu[6]=2になる。つまり2種類の素因数を持つ
sosu=[0]*(N+1)
for i in range(2,N+1):
    if sosu[i]==0:
        for j in range(i,N+1,i):
            sosu[j]+=1
            
#print(sosu[:30])

#iがK種類以上の素因数を持つならsを+1する
s=0
for i in sosu:
    if i>=K:
        s+=1
        
print(s)
