import math

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for j in range(m):
    gcd = a[0] + b[j]
    for i in range(1, n):
        gcd = math.gcd(gcd, a[i] + b[j])
    print(gcd, end=" ")