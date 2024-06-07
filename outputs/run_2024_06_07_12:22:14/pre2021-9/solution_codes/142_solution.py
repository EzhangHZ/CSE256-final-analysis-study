for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    x = [0] * n
    y = [0] * n

    for i in range(n):
        x[i] = a[i]
        y[i] = b[i]

    print(' '.join(map(str, x)))
    print(' '.join(map(str, y)))