#入力
x,y=map(int,input().split())

#全員同じとき
if x==y:
    print(x)
#三者三様
else:
    for i in range(3):
        if i!=x and i!=y:
            print(i)
