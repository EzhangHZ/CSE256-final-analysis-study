# Solution Code:

for _ in range(int(input())):
    n = int(input())
    final_digits = list(map(int, input().split()))
    moves = []
    for _ in range(n):
        b, moves_str = input().split()
        b = int(b)
        moves.append((b, moves_str))
    
    initial_sequence = []
    for i in range(n):
        current_digit = final_digits[i]
        for j in range(len(moves[i][1])):
            move = moves[i][1][j]
            if move == 'U':
                current_digit = (current_digit - 1) % 10
            else:
                current_digit = (current_digit + 1) % 10
        initial_sequence.append(current_digit)
    
    print(' '.join(map(str, initial_sequence)))