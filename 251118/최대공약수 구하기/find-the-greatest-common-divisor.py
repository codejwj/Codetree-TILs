n, m = map(int, input().split())

def print_max(x, y):
    for i in range(1, 101):
        if x % i == 0 and y % i == 0:
            max_i = 1
            if max_i <= i:
                max_i = i

    print(max_i)

print_max(n, m)