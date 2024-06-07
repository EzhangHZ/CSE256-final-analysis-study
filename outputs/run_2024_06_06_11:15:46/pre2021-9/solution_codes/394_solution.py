from collections import defaultdict

def count_valid_pair_combinations(boys, girls, pairs):
    boy_counts = defaultdict(int)
    girl_counts = defaultdict(int)
    for i in range(len(pairs)):
        boy_counts[pairs[i][0]] += 1
        girl_counts[pairs[i][1]] += 1

    total_combinations = 0
    for i in range(len(pairs)):
        total_combinations += len(pairs) - boy_counts[pairs[i][0]] - girl_counts[pairs[i][1]] + 1

    return total_combinations // 2

# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    a, b, k = map(int, input().split())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    
    pairs = [(boys[i], girls[i]) for i in range(k)]
    
    # Calculate and output the number of ways to choose two pairs that match the condition
    print(count_valid_pair_combinations(a, b, pairs))