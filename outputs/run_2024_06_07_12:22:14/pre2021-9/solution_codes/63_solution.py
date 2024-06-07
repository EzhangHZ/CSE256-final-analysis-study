n = int(input())
commands = input()

positions = set()
x = 0

for command in commands:
    if command == 'L':
        x -= 1
    elif command == 'R':
        x += 1
    positions.add(x)

print(len(positions))