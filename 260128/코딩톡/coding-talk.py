import sys

N, M, p = tuple(map(int, input().split()))
messages = []

for _ in range(M):
    c, u = input().split()
    messages.append((c, int(u)))

#확인하려는 p번째 메시지의 '안 읽은 사람의 수'를 기준으로 설정
target_unread = messages[p - 1][1]

#안 읽은 사람이 0명이면 모두가 읽은 것이므로 종료 
if target_unread == 0:
    sys.exit()

#확실하게 메시지를 읽은 사람들을 저장할 집합 
read_people = set()

for c, u in messages:
    #어떤 메시지의 안 읽은 사람의 수 u가 
    #확인하려는 메시지의 안 읽은 사람의 수보다 크거나 같다면
    #그 메시지를 보낸 사람 c는 최소한 p번째 메시지 시점의 채팅방에 있음 
    if u >= target_unread:
        read_people.add(c)

for i in range(N):
    person = chr(ord('A') + i)
    if not person in read_people:
        print(person, end = " ")