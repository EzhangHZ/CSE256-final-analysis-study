n, q = map(int, input().split())
s = input().strip()

for _ in range(q):
    l, r = map(int, input().split())
    sub = s[l-1:r]
    result = 0
    for i, char in enumerate(sub):
        result += (i+1) * sub.count(char)
    print(result)