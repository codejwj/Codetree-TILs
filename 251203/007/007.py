secret_code, meeting_point, time = tuple(input().split())

#클래스 선언
class Spy:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

s = Spy(secret_code, meeting_point, int(time))

print(f"secret code : {s.secret_code}")
print(f"meeting point : {s.meeting_point}")
print(f"time : {s.time}")