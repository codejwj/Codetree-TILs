#클래스 선언
class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []

for _ in range(5):
    codename, score = tuple(input().split())
    agents.append(Agent(codename, int(score)))

#최소 점수를 갖는 유저를 찾기
min_idx = 0
for i in range(1, 5):
    if agents[min_idx].score > agents[i].score:
        min_idx = i

print(agents[min_idx].codename, agents[min_idx].score)