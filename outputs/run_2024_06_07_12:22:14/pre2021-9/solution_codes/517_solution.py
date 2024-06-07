n = int(input())
subseq = []
p = 1
for i in range(1, n):
    p = (p * i) % n
    if p == 1:
        subseq = list(range(1, i + 1))

print(len(subseq))
print(" ".join(map(str, subseq)))