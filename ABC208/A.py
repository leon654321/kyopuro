#入力
A,B=map(int,input().split())

#6を出し続けてもBに到達しない。1を出し続けてもBを超えてしまう場合を除外する。
if A*6>=B and B>=A:
    print("Yes")
else:
    print("No")

