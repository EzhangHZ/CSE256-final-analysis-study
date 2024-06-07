for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()

    moves = 0
    chips_count = 0

    for i in range(n):
        if s1[i] == '*' and s2[i] == '*':
            chips_count += 2
        elif s1[i] == '*' or s2[i] == '*':
            chips_count += 1

    if chips_count == 1:
        moves = 0
    else:
        moves = chips_count - 1

    print(moves)