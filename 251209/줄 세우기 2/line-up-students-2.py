class Student:
    def __init__(self, h, w, num):
        self.h, self.w, self.num = h, w, num

n = int(input())
students = []
for i in range(1, n + 1):
    h, w = tuple(map(int, input().split()))
    students.append(Student(h, w, i))

students.sort(key = lambda x: (x.h, -x.w))

for student in students:
    print(student.h, student.w, student.num)