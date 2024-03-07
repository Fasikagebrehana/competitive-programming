from bisect import bisect_right
n = int(input())
price = list(map(int, input().split()))
q = int(input())
price.sort()

for _ in range(q):
    p = int(input())
    print(bisect_right(price, p))
    
            