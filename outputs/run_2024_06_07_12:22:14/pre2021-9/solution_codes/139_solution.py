for case in range(int(input())):
    n, m, r, c = map(int, input().split())
    max_rows = max(r-1, n-r)
    max_cols = max(c-1, m-c)
    print(max_rows + max_cols)