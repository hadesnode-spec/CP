t = int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))

    neg=a.count(-1)

    ans = 0
    if neg % 2 == 1:
        neg -= 1
        ans += 1
    while neg>n-neg:
        neg-=2
        ans+=2

    print(ans)