N = int(input())

def print_rect(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            print(cnt, end = " ")
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()

print_rect(N)