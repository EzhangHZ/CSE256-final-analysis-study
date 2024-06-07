for _ in range(int(input())):
    n = int(input())
    candies = list(map(int, input().split()))

    if max(candies) > sum(candies) // 2:
        print("NO")
        continue

    prev_type = -1
    max_candies = 0

    for idx, count in enumerate(candies):
        if count > max_candies:
            max_candies = count
            prev_type = idx

    if max_candies > 1:
        print("NO")
    else:
        print("YES")