import sys
myinput=sys.stdin.readline
def main():
    N=int(input())
    G=[[0]*1001 for _ in range(1001)]
    M=0
    m=10001
    for _ in range(N):
        x,y,X,Y=map(int,input().split())
        G[x][y]+=1
        G[X][Y]+=1
        G[x][Y]-=1
        G[X][y]-=1
        M=max([M,x,X,y,Y])
        m=min([m,x,X,y,Y])

    for i in range(m,M+1):
        for j in range(m+1,M+1):
            G[i][j]=G[i][j-1]+G[i][j]
    for j in range(m,M+1):
        for i in range(m+1,M+1):
            G[i][j]=G[i-1][j]+G[i][j]
    
    ans=[0]*(N+1)
    for i in range(m,M+1):
        for j in range(m,M+1):
            ans[G[i][j]]+=1
    for k in range(1,N+1):
        print(ans[k])
main()
