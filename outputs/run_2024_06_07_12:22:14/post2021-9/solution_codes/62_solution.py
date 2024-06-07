for _ in range(int(input())):
    n, m = map(int, input().split())
    distances = list(map(int, input().split()))

    energy_needed = 0
    for i in range(n):
        energy_to_travel = max(0, distances[i] - m) # Energy needed to travel the distance
        if m >= distances[i]: # If current energy is enough to travel the distance
            m -= distances[i] # Update current energy
        else: 
            energy_needed += distances[i] - m # Calculate energy needed to restore to reach the next bench
            m = 0 # Reset current energy to 0

    print(energy_needed)