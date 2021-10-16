#入力
N=int(input())
A=list(map(int,input().split()))

ans=[]

"""
A[i]<=A[i+1]　という状況を上り坂
A[i]>A[i+1]   を下り坂とする
金を最大化するためには下り坂のはじめで金を銀に交換して
下りが終わったら金に戻せばよい

実際、 a > b > c > d を満たす実数を用意してこれがAの下り坂に当てはまるとすると
金は a/b, a/c, a/d, b/c, b/d, c/d, (a/b)*(c/d) のいずれかに倍増する
このうち、 (a/b)*(c/d) = (a/d)*(c/b) < a/d であることを踏まえれば
a/dが最大となる

"""

i=0

flag=False    #Trueなら下ってる最中

while i<N:
    # 次が上り坂で、直前まで下っていた(flag=True)なら"1"を追加
    # 直前も登っていた(flag=False)なら"0"を追加
    if i<N-1 and A[i]<=A[i+1]:
        if flag:
            ans.append("1")
            flag=False      #次から登るので切り替え
        else:
            ans.append("0")
        i+=1
        
    # 次が下り坂で、直前も下っていた(flag=True)なら"1"を追加
    # 直前に登っていた(flag=False)なら"0"を追加
    elif i<N-1 and A[i]>A[i+1]:
        if flag:
            ans.append("0")
        else:
            ans.append("1")
            flag=True      #次から下るので切り替え
        i+=1
        
    # i=N-1のときの処理
    # それまで下っていたなら最後に金に変換
    # 登っていたなら何もしない
    else:
        if flag:
            ans.append("1")
        else:
            ans.append("0")
        i+=1

# 出力        
print(" ".join(ans))
