#入力
A,B=map(int,input().split())

if B-A<0: #AがBより大きい時
    print(0)
else: #上記以外
    print(B-A+1)
