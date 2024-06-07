for _ in range(int(input())):
    n = int(input())
    notes = list(map(int, input().split()))
    
    unique_notes = set()
    increase_count = 0
    
    for note in notes:
        if note in unique_notes:
            increase_count += 1
        else:
            unique_notes.add(note)
    
    max_diversity = len(unique_notes) + increase_count
    print(max_diversity)