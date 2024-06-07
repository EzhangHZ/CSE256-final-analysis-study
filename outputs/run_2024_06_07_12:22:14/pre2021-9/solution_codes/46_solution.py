for _ in range(int(input())):
    n = int(input())
    candies = list(map(int, input().split()))
    
    total_candies = sum(candies)
    if total_candies % n != 0:
        print(-1)
        continue
    
    target_candies = total_candies // n
    
    min_friends_needed = 0
    for candy_count in candies:
        if candy_count != target_candies:
            min_friends_needed += 1
    
    print(min_friends_needed)