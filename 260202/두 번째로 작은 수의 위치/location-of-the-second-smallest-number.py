n = int(input())
a = list(map(int, input().split()))

arr = list(set(a))
arr.sort()

if len(arr) < 2:
    print(-1)
elif a.count(arr[1]) >= 2:
    print(-1)
else:
    print(a.index(arr[1]) + 1)