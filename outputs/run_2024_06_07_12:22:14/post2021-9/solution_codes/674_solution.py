n = int(input())
MOD = 10**9 + 7

result = 0
for a in range(1, n-1):
    for b in range(1, n-a):
        c = n - a - b
        gcd_ab = math.gcd(a, b)
        lcm_c_gcd_ab = (c * gcd_ab) // math.gcd(c, gcd_ab)
        result = (result + lcm_c_gcd_ab) % MOD

print(result)