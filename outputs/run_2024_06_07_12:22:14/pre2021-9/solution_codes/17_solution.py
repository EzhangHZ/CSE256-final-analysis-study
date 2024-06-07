for _ in range(int(input())):
    n = int(input())
    candies = list(map(int, input().split()))

    total_weight = sum(candies)

    if total_weight % 2 != 0:
        print("NO")
        continue

    target_weight = total_weight // 2
    one_weight = candies.count(1)
    two_weight = candies.count(2)

    if target_weight % 2 == 0:
        if one_weight % 2 == 0 and two_weight % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if one_weight % 2 == 0 and two_weight % 2 == 0:
            print("YES")
        else:
            if one_weight >= 2 and two_weight % 2 == 1:
                print("YES")
            else:
                print("NO")