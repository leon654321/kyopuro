import sys
myinput=sys.stdin.readline

#入力
n,q=map(int,myinput().split())
A=list(map(int,myinput().split()))

"""
変数shiftに回数を記録しておけば列全体を変更しなくても
A[x+shift]で位置を指定できる
ex.一回右シフトするなら shift = -1 として列の先頭はA[0+shift]=A[-1]となる
"""

#シフトした回数
shift=0

for _ in range(q):
    t,x,y=map(int,myinput().split())
    x,y=x-1,y-1
    
    # 問題文の通り素直に入れ替え
    if t==1:
        A[x+shift],A[y+shift]=A[y+shift],A[x+shift]
    # シフトさせるただし列の長さを超える値になったら+nする
    elif t==2:
        shift-=1
        if shift<-n:
            shift+=n
    # 出力
    elif t==3:
        print(A[x+shift])
    
