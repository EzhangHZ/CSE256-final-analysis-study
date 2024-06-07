import math

def gcd(x, y):
    return math.gcd(x, y)

for _ in range(int(input())):
    n = int(input())
    songs = list(map(int, input().split()))
    del_songs = []

    last_listened = songs[0]

    for i in range(1, n):
        if gcd(last_listened, songs[i]) == 1:
            del_songs.append(songs[i])
        else:
            last_listened = songs[i]

    print(len(del_songs), *del_songs)