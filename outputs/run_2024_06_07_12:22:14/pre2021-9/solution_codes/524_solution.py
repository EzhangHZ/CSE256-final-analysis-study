for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    operations = 0
    sorted_a = sorted(a)

    for i in range(n):
        if a[i] > x:
            if a[i] not in sorted_a:
                operations = -1
                break
            a[i], x = x, a[i]
            operations += 1

    print(operations)