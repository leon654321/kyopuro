#https://atcoder.jp/contests/typical90/tasks/typical90_f
"""

"""

N,K=map(int,input().split())
S=input()
ans=""
#文字列を数字に変換して大小比較できるようにした
num=[ord(S[i]) - ord('a') + 1 for i in range(len(S))]
#print(num)

I_s=0
for i in reversed(range(K)):
    #print(num[I_s:N-i])
    #I_s+1文字目からN-i文字目までの中で最小の字を探索
    nnum=num[I_s:N-i]
    m=min(nnum)
    
    #最小の文字をansに追加してそのindexの次のindexをI_sに指定これをK回繰り返す
    n=nnum.index(m)
    ans+=S[n+I_s]
    I_s+=n+1
    
print(ans)
