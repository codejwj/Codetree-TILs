N = int(input())
segments = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

def intersecting(x1, x2):
    for i in range(N):
        for a, b in segments:
            if x2 < a or b < x1:
                return False
            else:
                return True

flag = True
for i in range(N):
    for x1, x2 in segments:
        if intersecting(x1, x2):
            flag = True
        else:
            flag = False

if flag:
    print("Yes")
else:
    print("No")