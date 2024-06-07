import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def adjacent(x, y):
    return (lcm(x, y) // gcd(x, y)) == int(math.sqrt(lcm(x, y) // gcd(x, y)))**2

def adjacent_elements(arr):
    n = len(arr)
    adjacent_count = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and adjacent(arr[i], arr[j]):
                adjacent_count[i] += 1
    return max(adjacent_count)

def array_transformation(arr, seconds):
    n = len(arr)
    for _ in range(seconds):
        new_arr = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if adjacent(arr[i], arr[j]):
                    prod *= arr[j]
            new_arr.append(prod)
        arr = new_arr
    return arr

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        w = int(input())
        beauty = array_transformation(arr, w)
        print(adjacent_elements(beauty))