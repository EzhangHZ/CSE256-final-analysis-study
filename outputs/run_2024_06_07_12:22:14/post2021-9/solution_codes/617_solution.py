n, k = map(int, input().split())

MOD = 10**9 + 7

def power(x, y):
    res = 1
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        y //= 2
    return res

# Calculate the minimum possible winner number
ans = 2
for i in range(2, n+1):
    ans = (ans + power(2, max(0, i-2)) * min(k, power(2, i-1) - 1)) % MOD

print(ans)