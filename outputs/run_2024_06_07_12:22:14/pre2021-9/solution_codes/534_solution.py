for _ in range(int(input())):
    n, l, r, s = map(int, input().split())
    total_sum = (r-l+1)*(r+l)//2

    if total_sum > s or s > (r-l+1)*n+(r-l)*(r-l+1)//2:
        print(-1)
    else:
        rem_sum = s - total_sum
        a = [i for i in range(1, n+1)]
        for i in range(r, l-1, -1):
            if rem_sum >= n-i:
                idx = a.index(i)
                a.remove(i)
                a.insert(idx-(n-i),i)
                rem_sum -= n-i
        print(*a)