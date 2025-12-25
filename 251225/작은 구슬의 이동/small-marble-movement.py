N, T = map(int, input().split())
R, C, D = input().split()
R, C = int(R) - 1, int(C) - 1

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[D]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

for _ in range(T):
    nr, nc = R + dxs[move_dir], C + dys[move_dir]
    if in_range(nr, nc):
        R, C = nr, nc
    else:
        move_dir = 3 - move_dir

print(R + 1, C + 1)