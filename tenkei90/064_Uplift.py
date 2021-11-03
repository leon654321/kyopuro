import sys
input=sys.stdin.readline

def main():
    # 入力（区画数、地殻変動回数）、標高
    N,Q=map(int,input().split())
    A=list(map(int,input().split()))
    
    # var[i]: 区画i+1と区画iとの標高差
    var=[0]*(N-1)
    for i in range(N-1):
        var[i]=A[i+1]-A[i]

    # 最初の不便さ
    ans=sum([abs(i) for i in val])

    
    for _ in range(Q):
        L,R,V=map(int,input().split())
        L,R=L-1,R-1
        
        # 1番左の上昇や1番右の下降は意味がないのでそれ以外で逐次計算
        if L!=0:
            # 区画Lと区画L-1の標高差を1度ansから差し引く
            ans-=abs(var[L-1])
            
            # 標高差に地殻変動を反映
            var[L-1]+=V
            
            # 答えに不便さを追加
            ans+=abs(var[L-1])
        
        # 上記とほぼ同じ
        if R!=N-1:
            ans-=abs(var[R])
            var[R]-=V
            ans+=abs(var[R])
            
        # 出力
        print(ans)

main()
