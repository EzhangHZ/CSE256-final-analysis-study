for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    counts = {}
    for num in a:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    winner = -1
    for i in range(n):
        if counts[a[i]] == 1 and a.count(a[i]) == 1:
            winner = i + 1
            break
    print(winner)