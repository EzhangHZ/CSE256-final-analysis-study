for _ in range(int(input())):
    n = int(input())
    tasks = input().strip()

    solved = set()
    suspicious = False

    for day in range(n):
        if tasks[day] in solved:
            suspicious = True
            break
        solved.add(tasks[day])

    if suspicious:
        print("NO")
    else:
        print("YES")