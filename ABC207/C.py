#入力
N=int(input())

A=[[0,0,0] for _ in range(N)]
for i in range(N):
    t,l,r=map(int,input().split())
    A[i]=[t,l,r] 

Ans=0
for i in range(N-1):
    ans=N-1-i # iに対するjの取りうる組み合わせの最大値
    for j in range(i+1,N): #各jに対して区間が重なるか判定する、開区間、閉区間は<=などで表現する。
        if A[i][0]==1:
            if A[j][0]==1 and (A[i][1]>A[j][2] or A[i][2]<A[j][1]):
                ans-=1
            elif A[j][0]==2 and (A[i][1]>=A[j][2] or A[i][2]<A[j][1]):
                ans-=1
            elif A[j][0]==3 and (A[i][1]>A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
            elif A[j][0]==4 and (A[i][1]>=A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
        elif A[i][0]==2:
            if A[j][0]==1 and (A[i][1]>A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
            elif A[j][0]==2 and (A[i][1]>=A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
            elif A[j][0]==3 and (A[i][1]>A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
            elif A[j][0]==4 and (A[i][1]>=A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
        elif A[i][0]==3:
            if A[j][0]==1 and (A[i][1]>=A[j][2] or A[i][2]<A[j][1]):
                ans-=1
            elif A[j][0]==2 and (A[i][1]>=A[j][2] or A[i][2]<A[j][1]):
                ans-=1
            elif A[j][0]==3 and (A[i][1]>=A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
            elif A[j][0]==4 and (A[i][1]>=A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
        elif A[i][0]==4:
            if (A[i][1]>=A[j][2] or A[i][2]<=A[j][1]):
                ans-=1
    #この時点でansには「iからスタートした時の値(すべてのjに関する情報)が入っている」   
    Ans+=ans
    
print(Ans)
