# Solution Code:

for _ in range(int(input())):
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        p[x] = p[y] = 1

    count = 0
    for i in range(1, n + 1):
        l = r = i
        while r <= n and p[r] == 0:
            r += 1
        count += (r - l) * (r - l + 1) // 2
        while r <= n:
            l = r
            while l <= n and p[l] == 1:
                l += 1
            if l <= n:
                r = l
                while r <= n and p[r] == 0:
                    r += 1
                count += (r - l) * (r - l + 1) // 2

    print(count)