n, m, k = map(int, input().split())

total_roads = 4*n*m - 2*n - 2*m

if k > total_roads:
    print("NO")
else:
    print("YES")

    def get_moves(row, col):
        moves = ""
        if row > 1:
            moves += "U" * (row - 1)
        if col > 1:
            moves += "L" * (col - 1)
        return moves

    steps = []
    while k > 0 and n > 1 and m > 1:
        if k >= m-1:
            steps.append((m-1, "R"))
            k -= m-1
            steps.append((1, "D" + "R"*(m-1)))
            k -= 1
        elif k >= n-1:
            steps.append((n-1, "D"))
            k -= n-1
            steps.append((1, "R" + "D"*(n-1)))
            k -= 1
        else:
            steps.append((k, "R"))
            k = 0

    print(len(steps))
    for step in steps:
        print(step[0], step[1])