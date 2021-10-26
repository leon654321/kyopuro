import sys
myinput=sys.stdin.readline

# 入力
n=int(myinput())
# 46の倍数であるかが重要なので剰余を扱う
A=[i%46 for i in list(map(int,myinput().split()))]
B=[i%46 for i in list(map(int,myinput().split()))]
C=[i%46 for i in list(map(int,myinput().split()))]

# A,B,Cに登場する46種類の数字についてその出現回数を記録する
A_num=[0]*46
B_num=[0]*46
C_num=[0]*46

for i in range(N):
    A_num[A[i]]+=1
    B_num[B[i]]+=1
    C_num[C[i]]+=1

#答え
ans=0

# i+j+k が46の倍数なら各数字の登場回数の積だけansに追加
# 三重ループだが計算量はO(10^5)
for i,a_num in enumerate(A_num):
    for j,b_num in enumerate(B_num):
        for k,c_num in enumerate(C_num):
            x=i+j+k
            if x==0 or x==46 or x==92:
                ans+=a_num*b_num*cn_num
        
# 出力
print(ans)
