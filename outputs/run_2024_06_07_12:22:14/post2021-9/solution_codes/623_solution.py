for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    threshold = max(b)
    a = [0] * n

    for i in range(n):
        if b[i] <= threshold:
            a[b[i] - 1] = i + 1
        else:
            for j in range(i-1, -1, -1):
                if b[j] <= threshold:
                    a[b[j] - 1] = i + 1
                    break

    print(threshold)
    print(*a)