n = int(input())
heroes_strength = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    max_defense_hero = max((hero for hero in heroes_strength if hero >= x))
    coins_needed = max(0, y - sum(hero for hero in heroes_strength if hero < x))
    coins_needed += max(0, x - max_defense_hero + 1)
    print(coins_needed)