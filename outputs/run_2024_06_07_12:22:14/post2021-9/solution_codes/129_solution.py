def generate_permutations(n):
    if n == 3:
        return [[1, 3, 2], [2, 1, 3], [3, 1, 2]]
    else:
        prev_permutations = generate_permutations(n-1)
        permutations = []
        for perm in prev_permutations:
            for i in range(n):
                new_perm = perm[:i] + [n] + perm[i:]
                valid = True
                for j in range(2, n):
                    if new_perm[j-2] + new_perm[j-1] == new_perm[j]:
                        valid = False
                        break
                if valid:
                    permutations.append(new_perm)
        return permutations

for _ in range(int(input())):
    n = int(input())
    permutations = generate_permutations(n)
    for perm in permutations[:n]:  # Print only n distinct anti-Fibonacci permutations
        print(' '.join(map(str, perm)))