import sys

INT_MAX = sys.maxsize
MAX_K = 10000

N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def get_cost(low, high):
    cost = 0
    for elem in arr:
        if elem < low:
            cost += low - elem
        elif elem > high:
            cost += elem - high

    return cost

min_cost = INT_MAX
for num in range(1, MAX_K + 1):
    min_cost = min(min_cost, get_cost(num, num + K))

print(min_cost)