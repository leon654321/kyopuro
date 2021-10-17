N=int(input())
ls=[list(map(int,input().split())) for _ in range(N)]

all_time=0

for i in range(N):
    all_time+=ls[i][0] / ls[i][1]
    
half=all_time/2
I=0
for i in range(N):
    half-=ls[i][0] / ls[i][1]
    if half<=0:
        I=i
        half=all_time/2
        break
        
for i in range(I):
    half-=ls[i][0] / ls[i][1]

ans=0

for i in range(I):
    ans+=ls[i][0]
    
ans+=half*ls[I][1]

print(ans)
