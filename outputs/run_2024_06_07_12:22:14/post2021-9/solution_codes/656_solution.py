import math

N, P = map(float, input().split())
maps_to_study = int(N - math.ceil(N * (1 - P)))
print(maps_to_study)