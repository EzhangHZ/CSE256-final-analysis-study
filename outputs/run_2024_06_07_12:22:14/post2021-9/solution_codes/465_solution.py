def f(x):
    count_1 = x.count('1')
    count_0 = len(x) - count_1
    if count_1 < (len(x) + 1) // 2 or count_0 < (len(x) + 1) // 2:
        return 0
    return pow(2, count_0-1, 998244353)

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    answer = 0
    mod = 998244353

    for i in range(1, n+1):
        answer = (answer + f(s[:i])) % mod

    print(answer)