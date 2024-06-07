for _ in range(int(input())):
    n = int(input())
    tokens = list(map(int, input().split()))
    count = 0

    for i in range(n):
        while tokens[i] % 2 == 0:
            count += 1
            tokens[i] //= 2

    print(count)