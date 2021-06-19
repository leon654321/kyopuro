N,K=map(int,input().split())
S=input()
ans=""
num=[ord(S[i]) - ord('a') + 1 for i in range(len(S))]
#print(num)
I_s=0
for i in reversed(range(K)):
    #print(num[I_s:N-i])
    nnum=num[I_s:N-i]
    m=min(nnum)
    n=nnum.index(m)
    ans+=S[n+I_s]
    I_s+=n+1
print(ans)
