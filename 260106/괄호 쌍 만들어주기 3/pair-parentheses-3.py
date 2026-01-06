A = input()

open_cnt = 0
total_pairs = 0

for elem in A:
    if elem == '(':
        open_cnt += 1
    elif elem == ')':
        total_pairs += open_cnt

print(total_pairs)