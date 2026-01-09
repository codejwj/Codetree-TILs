import sys

arr = [
    list(map(int, input().split())) 
    for _ in range(19)
]

def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19

dxs = [0, 1, 1, -1]
dys = [1, 0, 1, 1]

for r in range(19):
    for c in range(19):
        if arr[r][c] == 0:
            continue

        for dx, dy in zip(dxs, dys):
            all_same = True

            for k in range(1, 5):
                nx, ny = r + dx * k, c + dy * k
                if not in_range(nx, ny) or arr[nx][ny] != arr[r][c]:
                    all_same = False
                    break
        
            if all_same:
                print(arr[r][c])
                mid_r, mid_c = r + dx * 2 + 1, c + dy * 2 + 1
                print(mid_r, mid_c)
                sys.exit()

print(0)