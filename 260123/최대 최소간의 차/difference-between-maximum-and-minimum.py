MAX_NUM = 10000

N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

min_cost = MAX_NUM 
for a in range(1, MAX_NUM + 1):
    cost = 0
    for elem in arr:
        if a <= elem and elem <= a + K:
            continue
        elif elem < a:
            cost += (a - elem)
        else: #elem > a + K
            cost += elem - (a + K)
    
    min_cost = min(min_cost, cost)

print(min_cost)