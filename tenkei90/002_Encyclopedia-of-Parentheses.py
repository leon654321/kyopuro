#2  Encyclopedia of Parentheses（★3）AC
#https://atcoder.jp/contests/typical90/tasks/typical90_b
#このときはpermutationを知らなかったためwhile文を使ってそれらしきものを実装した

N=int(input())
if N%2==0:
    n=N//2
    S="("*n + ")"*n
    S=list(S)
    S_end="()"*n
    S_end=list(S_end)
    
    pos=[i for i in range(n)]
    #print(pos)
    
    if N!=2:
        while not (S==S_end):
            S=")"*N
            S=list(S)
            #print(pos)
            for x in pos:
                S[x]="("
            print("".join(map(str,S)))
            #print(pos)
            c=0
            i=n-1
            while c==0:
                if pos[i]!=(i*2):
                    if i==n-1:
                        pos[i]+=1
                        c=1
                    elif pos[i]!=(pos[i+1]-1):
                        pos[i]+=1
                        c=1
                    else:
                        c=1
                else:
                    i-=1
                    if pos[i]!=(i*2):
                        pos[i:]=[(pos[i]+j+1) for j in range(n-i)]
                        c=1
                        #print("a"+str(pos))
                    
                    
                    
    elif N==2:
        print("()")
