N,K=map(int,input().split())

Ls=[ -1 for _ in range(N)]
Rs=[ -1 for _ in range(N)]

nums=set([i for i in range(K)])

for i in range(K):
    c,k=input().split()
    k=int(k)-1
    if c=="L":
        Ls[k]=i
        nums.discard(i)
    elif c=="R":
        Rs[k]=i
#print(Ls,Rs)
ans=1

for i in range(N):
    #print(nums)
    if Ls[i]!=-1:
        nums.add(Ls[i])
    elif Rs[i]!=-1:
        nums.discard(Rs[i])
    else:
        ans*=len(nums)
        ans%=998244353

print(ans)
