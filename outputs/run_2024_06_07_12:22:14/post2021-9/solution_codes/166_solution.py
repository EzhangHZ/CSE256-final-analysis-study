# Solution Code:

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ops = 0

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                a[j] = 0
                ops += 1
            else:
                min_val = min(a[i], a[j])
                a[i] = min_val
                a[j] = min_val
                ops += 2

    print(ops)