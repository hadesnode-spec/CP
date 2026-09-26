t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = {}

    for x in a:
        freq[x]=freq.get(x, 0) + 1

    if len(freq)==1:
        print("Yes")
    elif len(freq)==2:
        counts = list(freq.values())

        if abs(counts[0]-counts[1])<=1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")