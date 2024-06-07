import bisect

def mex(arr):
    for i in range(len(arr) + 1):
        if i not in arr:
            return i

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    b = []
    
    while a:
        k = 1
        while mex(a[:k]) == k-1:
            k += 1
        b.append(mex(a[:k-1]))
        a = a[k-1:]

    print(len(b))
    print(*b)