for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    
    min_sum = 0
    for i in range(n - 1):
        min_sum += int(s[i:i+2], 2)

    if k == 0:
        print(min_sum)
        continue

    ones_count = s.count('1')
    diff = min(2 * k, ones_count)
    potential_decrease = diff * (diff + 1) // 2
    print(min_sum - potential_decrease)