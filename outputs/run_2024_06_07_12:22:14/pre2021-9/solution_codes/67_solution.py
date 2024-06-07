for _ in range(int(input())):
    n = int(input())
    reviewers = list(map(int, input().split()))
    
    count_first_server = 0
    count_second_server = 0
    
    for reviewer in reviewers:
        if reviewer == 1:
            count_first_server += 1
        elif reviewer == 2:
            count_second_server += 1
        else:
            if count_first_server > count_second_server:
                count_second_server += 1
            else:
                count_first_server += 1
                
    total_upvotes = count_first_server + count_second_server
    print(total_upvotes)