import math

T = int(input())

for _ in range(T):
    n = int(input())
    side_length = 1 / math.sin(math.pi/(2*n))
    print("{:.9f}".format(side_length))