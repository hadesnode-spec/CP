t=int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a!=sorted(a):
        print(0)
    else:
        gaps=[]

        for i in range(n-1):
            gaps.append(a[i+1]-a[i])

        m=min(gaps)

        print(m//2+1)