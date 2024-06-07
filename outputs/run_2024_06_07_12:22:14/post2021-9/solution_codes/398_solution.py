for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) % n != 0:
        print("No")
        continue

    c = 0
    target = 0
    for i in range(n):
        target += a[i] - i
        if target < 0 or target % n == 0:
            c += 1

    if c > 0:
        print("No")
    else:
        print("Yes")