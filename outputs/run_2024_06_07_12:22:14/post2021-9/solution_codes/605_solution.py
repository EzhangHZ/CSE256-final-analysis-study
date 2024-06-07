MOD = 998244353

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def is_ambiguous(arr):
    n = len(arr)
    seen = set()
    for i in range(n):
        curr_gcd = gcd(arr[i], i + 1)
        if curr_gcd in seen:
            return True
        seen.add(curr_gcd)
    return False

def count_ambiguous_arrays(n, m):
    count = 0
    for length in range(1, n + 1):
        for i in range(1, m + 1):
            arr = [i] * length
            if is_ambiguous(arr):
                count += 1
    return count % MOD

n, m = map(int, input().split())
result = count_ambiguous_arrays(n, m)
print(result)