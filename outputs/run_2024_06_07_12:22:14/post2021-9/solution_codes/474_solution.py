for _ in range(int(input())):
    n, m, k = map(int, input().split())
    field = [list(input()) for _ in range(n)]

    def is_valid(i, j):
        return 0 <= i < n and 0 <= j < m

    def check_tick(i, j, size):
        if not is_valid(i, j) or field[i][j] == '.':
            return False
        for h in range(0, size+1):
            if not is_valid(i-h, j-h) or field[i-h][j-h] != '*' or not is_valid(i-h, j+h) or field[i-h][j+h] != '*':
                return False
        return True

    valid = True
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                tick_size = max(abs(i-n//2), abs(j-m//2))
                if tick_size < k:
                    valid = False
                else:
                    if not check_tick(i, j, tick_size):
                        valid = False

    if valid:
        print("YES")
    else:
        print("NO")