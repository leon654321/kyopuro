# 入力
X=input()

# すべて同じ文字の場合
if X[0]==X[1] and X[1]==X[2] and X[2]==X[3]:
    print("Weak")
else:
    # 四つの数が連続した時の判定
    # 各数字間が連続すると a+=1 つまり全部連続なら a=3
    a=0
    for i in range(3):
        if int(X[i])+1==int(X[i+1]):
            a+=1
        elif X[i]=="9" and X[i+1]=="0":
            a+=1
    
    # 連続した数字のとき
    if a==3:
        print("Weak")
    # そうでないとき
    else:
        print("Strong")
