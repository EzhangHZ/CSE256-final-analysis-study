# Solution Code:

N, M = map(int, input().split())

horizontal_dominoes = (M * N) - M
vertical_dominoes = (N - 1) * M

total_dominoes = horizontal_dominoes + vertical_dominoes

print(total_dominoes)