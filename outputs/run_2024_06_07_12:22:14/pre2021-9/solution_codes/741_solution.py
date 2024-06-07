from collections import deque

# Helper function to find the lexicographically smallest triple for given xor
def find_smallest_triple(x):
    a, b, c = 1, 1, x
    while a & b != 0 or a == x:
        a *= 2
        b = x ^ a
    return a, b, c

# Generate the infinite sequence 's'
s = []
seen = set()
queue = deque([(1, 1, 1)])
while len(s) < 10**6:
    a, b, c = queue.popleft()
    s.append(a)
    s.append(b)
    s.append(c)
    seen.add((a, b, c))
    if (a+1, b, c) not in seen:
        queue.append((a+1, b, c))
    if (a, b+1, c) not in seen:
        queue.append((a, b+1, c))
    if (a, b, c+1) not in seen:
        queue.append((a, b, c+1))

# Process test cases
t = int(input())
for _ in range(t):
    n = int(input())
    print(s[n-1])