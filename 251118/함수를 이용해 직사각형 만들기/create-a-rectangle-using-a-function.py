n, m = map(int, input().split())

def print_rect(x, y):
    for _ in range(x):
        print("1" * y)

print_rect(n, m)