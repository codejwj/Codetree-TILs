MAX_NUN = 10000

N = int(input())
ranges = [
    tuple(map(int, input().split())) 
    for _ in range(N)
]

def satisfied(x):
    for a, b in ranges:
        #계속 2배씩 해주며
        #a <= x <= b를 항상 만족하는지 확인
        #아니라면, False를 반환
        x *= 2
        if x < a or x > b:
            return False
        
    return True

#1 ~ MAX_NUN 사이에 대해 탐색
for i in range(1, MAX_NUN + 1):
    #만족하는 i가 있다면, 해당 i가 최소이므로 출력
    if satisfied(i):
        print(i)
        break