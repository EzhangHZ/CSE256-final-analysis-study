for case in range(int(input())):
    n, m = map(int, input().split())
    friends_available = []
    for _ in range(m):
        friends_available.append(list(map(int, input().split()[1:]))

    chosen_friends = {}
    output = []
    for friends_day in friends_available:
        chosen_friend = -1
        for friend in friends_day:
            if friend not in chosen_friends:
                chosen_friends[friend] = 1
                chosen_friend = friend
                break
            elif chosen_friends[friend] < (m + 1) // 2:
                chosen_friends[friend] += 1
                chosen_friend = friend
                break
        output.append(chosen_friend)

    if len(output) == m:
        print("YES")
        print(*output)
    else:
        print("NO")