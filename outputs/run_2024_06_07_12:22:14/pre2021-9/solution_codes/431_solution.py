import heapq

q = int(input())
customers = []
money_queue = []
served = []

for i in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        customers.append(i+1)
        heapq.heappush(money_queue, (-query[1], i+1))
    elif query[0] == 2:
        served.append(customers[0])
        customers.pop(0)
    elif query[0] == 3:
        while money_queue[0][1] not in customers:
            heapq.heappop(money_queue)
        served.append(money_queue[0][1])
        customers.remove(money_queue[0][1])
        heapq.heappop(money_queue)

for customer in served:
    print(customer, end=' ')