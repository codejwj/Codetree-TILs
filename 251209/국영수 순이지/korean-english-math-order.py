class Student:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
studnets = [Student(name, int(kor), int(eng), int(math)) for name, kor, eng, math in arr]

studnets.sort(key = lambda x: (-x.kor, -x.eng, -x.math))

for student in studnets:
    print(student.name, student.kor, student.eng, student.math)