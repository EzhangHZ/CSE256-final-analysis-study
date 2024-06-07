for _ in range(int(input())):
    n, k, m = map(int, input().split())
    b = list(map(int, input().split()))

    if m > n:
        print("NO")
        continue
    
    if m == n:
        if b == list(range(1, n+1)):
            print("YES")
        else:
            print("NO")
        continue

    max_remove = (k - 1) // 2

    idx_b = 0
    cnt_not_removed = 0
    for i in range(1, n+1):
        if idx_b < m and b[idx_b] == i:
            idx_b += 1
        else:
            if cnt_not_removed < max_remove:
                cnt_not_removed += 1
            else:
                print("NO")
                break
    else:
        print("YES")