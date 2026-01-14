N = int(input())
points = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

#삼각형의 넓이에 2를 곱한 값을 반환
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))

max_area = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            #x값이 같은 쌍이 있으며, y값 역시 같은 쌍이 있는 경우에만 최대 넓이를 계산
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]

            if (x1 == x2 or x2 == x3 or x3 == x1) and (y1 == y2 or y2 == y3 or y3 == y1):
                max_area = max(max_area, area(x1, y1, x2, y2, x3, y3))
        
print(max_area)