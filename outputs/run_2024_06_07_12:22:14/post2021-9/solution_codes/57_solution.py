for _ in range(int(input())):
    n = int(input())
    winner = 1
    for _ in range(n):
        if winner % 2 == 1:
            winner = winner // 2 + 1
        else:
            winner = winner // 2**(winner.bit_length() - 1) + 2**(winner.bit_length() - 1) - winner
    print(winner)