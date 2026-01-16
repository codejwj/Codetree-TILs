N, M, D, S = tuple(map(int, input().split()))

eat_recodes = []
for _ in range(D):
    eat_recodes.append(list(map(int, input().split())))

sick_dict = {}
for _ in range(S):
    p, t = tuple(map(int, input().split()))
    sick_dict[p] = t

ans = 0
for i in range(1, M + 1):
    is_possible = True

    for person, sick_time in sick_dict.items():
        ate_before = False
        for p, m, t in eat_recodes:
            if p == person and m == i and t < sick_time:
                ate_before = True
                break

        if not ate_before:
            is_possible = False
            break
    
    if is_possible:
        eaters = set()
        for p, m, t in eat_recodes:
            if m == i:
                eaters.add(p)
        
        ans = max(ans, len(eaters))

print(ans)