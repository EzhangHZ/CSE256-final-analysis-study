def find_secret_integer(l, r, final_array):
    for x in range(1 << 17):
        original_array = [(i ^ x) for i in range(l, r+1)]
        if original_array == final_array:
            return x

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    final_array = list(map(int, input().split()))
    secret_integer = find_secret_integer(l, r, final_array)
    print(secret_integer)