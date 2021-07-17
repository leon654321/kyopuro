#入力
ls=list(map(int,input().split()))

#昇順並び替え
ls=sorted(ls)

#後ろ二つの和をとる
print(ls[1]+ls[2])
