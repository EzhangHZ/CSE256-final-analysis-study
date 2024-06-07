import math

def find_values(l, r, m):
    for a in range(l, r+1):
        if (m - a + l) % a == 0:
            n = (m - l + a) // a
            b = l
            c = l
            print(a, b, c)
            return

t = int(input())

for _ in range(t):
    l, r, m = map(int, input().split())
    find_values(l, r, m)