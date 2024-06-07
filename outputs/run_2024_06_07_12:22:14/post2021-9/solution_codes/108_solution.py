for _ in range(int(input())):
    n = int(input())
    moves = 0
    for _ in range(n):
        x, y = map(int, input().split())
        moves += abs(x) + abs(y)
    print(moves)