for _ in range(int(input())):
    n = int(input())
    alice_white, alice_black = 0, 0
    bob_white, bob_black = 0, 0
    i = 1
    while n > 0:
        if i % 2 == 1:
            dealt_cards = min(i, n)
            alice_white += dealt_cards // 2
            alice_black += dealt_cards - dealt_cards // 2
        else:
            dealt_cards = min(2*i, n)
            bob_white += dealt_cards // 2
            bob_black += dealt_cards - dealt_cards // 2
        n -= dealt_cards
        i += 1
    print(f"{alice_white} {alice_black} {bob_white} {bob_black}")