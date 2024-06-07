# Solution Code:
for _ in range(int(input())):
    path = input().strip()
    visited = set()
    time = 0

    for direction in path:
        if direction not in visited:
            visited.add(direction)
            time += 5
        else:
            time += 1

    print(time)