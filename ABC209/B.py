#入力
N,X=map(int,input().split())
A=list(map(int,input().split()))

#値引額
z=N//2

#所持金＋値引額ー定価が0円以上なら
if X+z-sum(A)>=0:
    print("Yes")
#0円以下なら
else:
    print("No")
