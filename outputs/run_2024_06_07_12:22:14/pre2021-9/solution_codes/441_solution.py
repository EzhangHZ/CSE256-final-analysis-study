def min_special_exchanges(n, perm):
    exchange_count = 0
    i = 1
    while i <= n:
        if perm[i-1] != i:
            j = i
            while j < n and perm[j] != j+1:
                j += 1
            exchange_count += 1
            i = j + 1
        else:
            i += 1
    return exchange_count

for _ in range(int(input())):
    n = int(input())
    perm = list(map(int, input().split()))
    
    if perm == sorted(perm):
        print(0)
    else:
        exchanges = min_special_exchanges(n, perm)
        print(exchanges)