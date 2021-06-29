#問題
#https://atcoder.jp/contests/typical90/tasks/typical90_bz

#入力
N,M=map(int,input().split())

#グラフ生成
G=[[]for _ in range(N)]

ans=0 #答え

for _ in range(M):
    a,b=map(int,input().split())
    if a<b:
        #相互にくっつけても時間を取るだけなので片方だけ
        G[b-1].append(a-1)
        
        #一番最初だけ＋１
        if len(G[b-1])==1:
            ans+=1
        #二つ目が表れたら最初の加算をなしにする
        elif len(G[b-1])==2:
            ans-=1
    else:
        G[a-1].append(b-1)
        if len(G[a-1])==1:
            ans+=1
        elif len(G[a-1])==2:
            ans-=1

print(ans)
