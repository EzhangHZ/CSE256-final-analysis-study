n, m, k = map(int, input().split())

pictures = []
for _ in range(k+1):
    picture = [input() for _ in range(n)]
    pictures.append(picture)
    if _ < k:
        input()  # Consume empty line between pictures

initial_picture_index = -1
operations = []

for i, picture in enumerate(pictures):
    black_count = sum(row.count('1') for row in picture)
    white_count = n * m - black_count

    if black_count == 0 or white_count == 0:
        initial_picture_index = i
        break

    operations.append(f"2 {i+1}")

for x in range(1, n-1):
    for y in range(1, m-1):
        if pictures[initial_picture_index][x][y] == '0':
            if pictures[initial_picture_index][x-1][y] == '1' and pictures[initial_picture_index][x+1][y] == '1' and pictures[initial_picture_index][x][y-1] == '1' and pictures[initial_picture_index][x][y+1] == '1':
                operations.append(f"1 {x+1} {y+1}")
        else:
            if pictures[initial_picture_index][x-1][y] == '0' and pictures[initial_picture_index][x+1][y] == '0' and pictures[initial_picture_index][x][y-1] == '0' and pictures[initial_picture_index][x][y+1] == '0':
                operations.append(f"1 {x+1} {y+1}")

print(initial_picture_index + 1)
print(len(operations))
for op in operations:
    print(op)