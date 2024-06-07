for _ in range(int(input())):
    n, m = map(int, input().split())
    scores = list(map(int, input().split()))
    
	# Calculate the current average score of the class
    avg_score = sum(scores) / n
    
	# Determine the maximum possible score you can assign to yourself
    max_score = min(m, avg_score + (n - 1))
    
    print(max_score)