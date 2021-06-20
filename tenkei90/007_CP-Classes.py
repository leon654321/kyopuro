#問題文
#https://atcoder.jp/contests/typical90/tasks/typical90_g

#全探索を行うと制約的にTLEになるので二分探索を行う
def binary_search(z, item):
    low = 0
    high = len(z) - 1

    while low <= high:
        mid = (low + high) //2
        guess1 = z[mid]
        guess2 = z[mid+1]
        if guess1<= item <=guess2:
            return mid
        if guess1 > item:
            high = mid -1
        else:
            low = mid + 1

    return None

n=int(input())
rate=list(map(int,input().split()))
#二分探索のためにAを昇順で並び替え
rate=sorted(rate,reverse=False)

q=int(input())

for _ in range(q):
    b=int(input())
    #この生徒のレートがどのクラスよりも低いとき
    if b<=rate[0]:
        print(rate[0]-b)
        
    #この生徒のレートがどのクラスよりも高いとき
    elif b>=rate[n-1]:
        print(b-rate[n-1])
        
    #この生徒のレートがAのどこに入るか二分探索。上下のクラスで差が小さい方がans
    else:
        i= binary_search(rate, b) 
        ans=[( b-rate[i] ) , ( rate[i+1]-b )]
        print(min(ans))
