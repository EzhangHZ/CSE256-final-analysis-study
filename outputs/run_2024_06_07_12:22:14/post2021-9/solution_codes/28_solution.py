from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print(n)
        continue

    n_str = str(n)
    min_changes = float('inf')
    possible_numbers = []

    for num_changes in range(1, len(n_str) + 1):
        for indices in combinations(range(len(n_str)), num_changes):
            new_num = ''.join(['7' if i in indices else n_str[i] for i in range(len(n_str))])
            if new_num[0] != '0' and int(new_num) % 7 == 0:
                possible_numbers.append(int(new_num))

    print(possible_numbers[0])