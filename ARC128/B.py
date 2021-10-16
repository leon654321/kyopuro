# 入力
T=int(input())

for _ in range(T):
    # 入力
    num=list(map(int,input().split()))
    
    # 昇順並び替え
    num.sort()
    
    # ある二組の数が同じなら普通にその数だけ移動させればよい
    # ex. 1 2 2 → 3 1 1 → 5 0 0
    if num[0]==num[1] or num[1]==num[2]:
        print(num[1])
        continue
    
    # 各項どうしの差を定義
    X=num[1]-num[0]
    Y=num[2]-num[1]
    Z=num[2]-num[0]
    
    
    # 最終的には 0 0 MAX の形にする
    # A A+3D B → A+2D A+2D B-D → 0 0 2A+B+3D
    if X%3==0:
        print(num[1])
        
    # MAX 0 0 の形にする
    # A B B+3D → A+2 B-1 B+3D-1 → A+1 B+1 B+1+3(D-1)
    # 上記の操作を繰り返すといずれ A' B' B' の形にできる
    elif X%3!=0 and Y%3==0:
        print(num[2])
    
    # 0 MAX 0 の形にする
    # 一つ上の方法と同じ考えで操作すればよい
    elif Z%3==0 and Y%3!=0:
        print(num[2])
        
    #どの項の差も三の倍数にならないとき
    else:
        print(-1)
