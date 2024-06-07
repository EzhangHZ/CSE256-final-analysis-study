n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])
else:
    max_circular_value = 0
    while n > 1:
        circular_values = []
        for i in range(n):
            circular_val = a[i-1] + a[(i+1) % n]
            circular_values.append(circular_val)
        max_circular_value = max(circular_values)
        max_index = circular_values.index(max_circular_value)
        a.pop(max_index)
        a.pop((max_index) % (n-1))
        a.insert(max_index, max_circular_value)
        n -= 2

    print(max_circular_value)