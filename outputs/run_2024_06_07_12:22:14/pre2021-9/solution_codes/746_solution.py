n, k = map(int, input().split())
c = list(map(int, input().split()))

max_score = 0

for i in range(n):
    temp_score = max_score + c[i]
    max_score = max(max_score, temp_score)

if k > 0:
    for i in range(n):
        temp_score = max_score + c[i]
        max_score = max(max_score, temp_score)
        max_score = max(max_score, 0)

print(max_score)