#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_bt

#1<=H,W<=16なので全探索で間に合う
#DFSを実装して愚直に最大ループを探すだけ

from copy import deepcopy
H,W=map(int,input().split())
G=["#"*(W+2) for _ in range(H+2)]

for i in range(1,H+1):
    G[i]="#"+input()+"#"

ans=-1    

for i in range(1,H+1):
    for j in range(1,W+1):
        i_s,j_s=i,j
        al=set([()])
        cnt=0
        
        
        def f(i_S,j_S,c,Al):
            global i,j,G,ans
            #print(c)
            #print(i_S,j_S)
            if i_S==i and j_S==j and c>0:
                if c>2:
                    ans=max(ans,c)
                    return
                else:
                    return
            if G[i_S+1][j_S]=="." and (i_S+1,j_S) not in Al:
                B=deepcopy(Al)
                B.add((i_S+1,j_S))
                f(i_S+1,j_S,c+1,B)
            if G[i_S-1][j_S]=="." and (i_S-1,j_S) not in Al:
                B=deepcopy(Al)
                B.add((i_S-1,j_S))
                f(i_S-1,j_S,c+1,B)
            if G[i_S][j_S+1]=="." and (i_S,j_S+1) not in Al:
                B=deepcopy(Al)
                B.add((i_S,j_S+1))
                f(i_S,j_S+1,c+1,B)
            if G[i_S][j_S-1]=="." and (i_S,j_S-1) not in Al:
                B=deepcopy(Al)
                B.add((i_S,j_S-1))
                f(i_S,j_S-1,c+1,B)
        
        f(i_s,j_s,cnt,al)

print(ans)

