import sys
input=sys.stdin.readline
#いもす法というらしいです。詳しくは[こちら](https://twitter.com/e869120/status/1388262816101007363)

def main():
    #入力
    N=int(input())
    G=[[0]*1001 for _ in range(1001)]
    
    #紙の角にマークを付ける
    for _ in range(N):
        x,y,X,Y=map(int,input().split())
        G[x][y]+=1
        G[X][Y]+=1
        G[x][Y]-=1
        G[X][y]-=1
        
    #j方向に累計和
    for i in range(0,1001):
        for j in range(0,1000):
            G[i][j+1]=G[i][j]+G[i][j+1]
    #i方向に累計和
    for j in range(0,1001):
        for i in range(0,1000):
            G[i+1][j]=G[i][j]+G[i+1][j]
    
    #平面上の各マスの値は積まれた紙の数(1~N)に対応するので、
    #例えばG[i][j]=Xならans[X]に+1すればよい
    ans=[0]*(N+1)
    for i in range(0,1001):
        for j in range(0,1001):
            ans[G[i][j]]+=1
            
    #出力
    for i in range(1,N+1):
        print(ans[i])
main()
