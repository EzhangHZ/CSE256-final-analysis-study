for case in range(int(input())):
    s, n = map(int, input().split())
    nums = []
    for i in range(n-1):
        if s > 1:
            nums.append(1)
            s -= 1
        else:
            nums.append(0)
    nums.append(s)
    print(*nums)