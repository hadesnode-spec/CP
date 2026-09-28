t=int(input())

for _ in range(t):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())

    moves = [
    (a, b), (a, -b),
    (-a, b), (-a, -b),
    (b, a), (b, -a),
    (-b, a), (-b, -a)
    ]

    king_positions = set()
    queen_positions = set()

    for dx, dy in moves:
        king_positions.add((xk + dx, yk + dy))
        queen_positions.add((xq + dx, yq + dy))
    print(len(king_positions & queen_positions))
