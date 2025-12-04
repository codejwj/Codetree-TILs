N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    if i % 2 == 0:
       new_arr = arr[:i + 1]

       new_arr.sort()
       
       print(new_arr[len(new_arr) // 2], end = " ")