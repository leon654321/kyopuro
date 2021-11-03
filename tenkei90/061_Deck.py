import sys
input=sys.stdin.readline

# Q<=10^5なので普通に処理すれば間に合う

# 入力（操作の数）
Q=int(input())

#山札
card=[]

for _ in range(Q):
    # 入力の1文字目に従い各操作を行う
    order,num=map(int,input().split())
    if order==1:
        card.insert(0,num)
    elif order==2:
        card.append(num)
    else:
        print(card[num-1])
