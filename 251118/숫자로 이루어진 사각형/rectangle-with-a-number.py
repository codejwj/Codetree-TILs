N = int(input())

def print_rect(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            print(cnt, end = " ")
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()

print_rect(N)