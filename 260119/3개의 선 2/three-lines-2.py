N = int(input())
points = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

x = list(set(p[0] for p in points))
y = list(set(p[1] for p in points))

candidates = []
for val in x:
    candidates.append(('x', val))
for val in y:
    candidates.append(('y', val))

def checked(l1, l2, l3):
    for px, py in points:
        on_l1 = (l1[0] == 'x' and px == l1[1]) or (l1[0] == 'y' and py == l1[1])
        on_l2 = (l2[0] == 'x' and px == l2[1]) or (l2[0] == 'y' and py == l2[1])
        on_l3 = (l3[0] == 'x' and px == l3[1]) or (l3[0] == 'y' and py == l3[1])
        
        if not (on_l1 or on_l2 or on_l3):
            return False
    
    return True

ans = 0
for l1 in candidates:
    for l2 in candidates:
        for l3 in candidates:
            if checked(l1, l2, l3):
                ans = 1
                break

print(ans)