for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = 0
    for num in arr:
        x ^= num
    print(x)