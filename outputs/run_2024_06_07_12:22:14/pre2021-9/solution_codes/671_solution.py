def check_subsequence_cost(a, k, mid):
    max_odd = float('-inf')
    max_even = float('-inf')
    count = 1
    for num in a:
        if count % 2 == 0:
            max_even = max(max_even, num)
        else:
            max_odd = max(max_odd, num)
        count += 1
    
    if count <= k:
        if max(max_odd, max_even) <= mid:
            return True
    else:
        new_count = k
        while new_count <= count:
            if max(max_odd, max_even) <= mid:
                return True
            if a[new_count-k] == max_odd:
                max_odd = max(a[new_count-k+1: new_count])
            if a[new_count-k] == max_even:
                max_even = max(a[new_count-k+1: new_count])
            new_count += 1
            
    return False

def minimum_cost_subsequence(n, k, a):
    low, high = 1, 10**9
    while low <= high:
        mid = (low + high) // 2
        if check_subsequence_cost(a, k, mid):
            high = mid - 1
        else:
            low = mid + 1

    return low

# Input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(minimum_cost_subsequence(n, k, a))