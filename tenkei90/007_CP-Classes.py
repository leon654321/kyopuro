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
rate=sorted(rate,reverse=False)

q=int(input())

for _ in range(q):
    b=int(input())
    if b<=rate[0]:
        print(rate[0]-b)
    elif b>=rate[n-1]:
        print(b-rate[n-1])
    else:
        i= binary_search(rate, b) 
        ans=[( b-rate[i] ) , ( rate[i+1]-b )]
        print(min(ans))
