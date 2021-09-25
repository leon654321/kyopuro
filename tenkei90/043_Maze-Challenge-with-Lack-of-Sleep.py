from collections import deque

def main():
    #入力
    H,W=map(int,input().split())
    i_s,j_s=map(int,input().split())
    i_g,j_g=map(int,input().split())
    
    #マップ作製（周囲に1マスずつ"#"の余裕を持たせている）
    G=["#"*(W+2) for _ in range(H+2)]

    for i in range(1,H+1):
        G[i]="#"+ input() +"#"

    #スタート地点を"#"に変更
    G[i_s]=G[i_s][:j_s]+"#"+G[i_s][j_s+1:]

    #方向転換の回数を管理
    turn=[[2**31-1]*((W+2)*(H+2)) for _ in range(4)]
    
    #スタート地点の方向転換数を設定
    turn[0][i_s*(W+2)+j_s]=0 #↑
    turn[1][i_s*(W+2)+j_s]=0 #→
    turn[2][i_s*(W+2)+j_s]=0 #↓
    turn[3][i_s*(W+2)+j_s]=0 #←

    
    ### BFSで解いていく###
    
    #移動先リスト
    nxt=deque([(i_s,j_s)])
    
    # ゴール地点の方向転数の最小値が答え
    ans=min( min(turn[0][i_g*(W+2)+j_g],turn[1][i_g*(W+2)+j_g]), min(turn[2][i_g*(W+2)+j_g],turn[3][i_g*(W+2)+j_g]) )
    
    #方向転換の微小量（ d(drection) ）
    dd=[(-1,0),(0,1),(1,0),(0,-1)] #マップ的に[↑、→、↓、←]


    while nxt:
        (i,j)=nxt.popleft()
        
        #ゴール地点のときの処理
        if i==i_g and j==j_g:
            ans=min( min(turn[0][i_g*(W+2)+j_g],turn[1][i_g*(W+2)+j_g]), min(turn[2][i_g*(W+2)+j_g],turn[3][i_g*(W+2)+j_g]) )
            continue
            
        # G[i][j]の方向転換数[↑、→、↓、←]
        direction = [ turn[0][i*(W+2)+j], turn[1][i*(W+2)+j], turn[2][i*(W+2)+j], turn[3][i*(W+2)+j] ]
        
        #現状の解以上の方向転換をしたときは終了
        if min(direction)>=ans:
            continue
        
        #現在の地点から上下左右を探索
        for num,(x,y) in enumerate(dd):
            #隣が通行可能なら
            if G[i+x][j+y]==".":
                
                #隣に移ることでそのマスの方向転換数が更新されるならTrue
                cnt=False
                
                #隣のマスの方向転換数管理
                #曲がる必要がないなら0、曲がるなら1
                dturn=[0 if k==num else 1 for k in range(4) ]
                
                #隣のマスの方向転換数が更新されるかチェック（更新されるならcnt=True）
                for k in range(4):
                    if turn[k][(i+x)*(W+2)+(j+y)] > direction[num]+dturn[k]:
                        cnt=True
                        break
                
                # 隣のマスの方向転換数を更新
                if cnt:
                    for k in range(4):
                        turn[k][(i+x)*(W+2)+(j+y)]=min(turn[k][(i+x)*(W+2)+(j+y)],direction[num]+dturn[k])
                        
                    #隣のマスを移動先リストに加える
                    nxt.append((i+x,j+y))

    #出力
    print(ans)
 
if __name__ == '__main__':
    main()
