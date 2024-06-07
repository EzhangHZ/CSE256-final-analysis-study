for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    locked = list(map(int, input().split()))

    unlocked = [x for x, l in zip(arr, locked) if l == 0]
    unlocked.sort()
    unlocked_idx = 0

    result = []
    for l in locked:
        if l == 1:
            result.append(str(arr[unlocked_idx]))
            unlocked_idx += 1
        else:
            result.append(str(unlocked.pop(0)))

    print(" ".join(result))