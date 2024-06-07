def count_strings(n):
    return n * (n - 1) // 2

def kth_string(n, k):
    result = ['a'] * (n - 2) + ['b', 'b']
    pos = count_strings(n)
    for i in range(n - 3, -1, -1):
        pos -= i
        if pos >= k:
            result[i] = 'b'
            break
    return ''.join(result)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(kth_string(n, k))