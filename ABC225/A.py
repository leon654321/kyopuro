#入力
S=input()

#3つとも同じ数字
if S[0]==S[1] and S[0]==S[2]:
    print(1)
#2種類の数字で構成される場合
elif S[0]==S[1] or S[0]==S[2] or S[1]==S[2]:
    print(3)
#3種類で構成
else:
    print(6)
