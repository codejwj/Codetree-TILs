class Student:
    def __init__(self, h, w, num):
        self.h, self.w, self.num = h, w, num

n = int(input())
students = []
for i in range(n):
    data = input().split()
    h = data[0]
    w = data[1]
    students.append(Student(int(h), int(w), i + 1))

students.sort(key = lambda x: (-x.h, -x.w, x.num))

for student in students:
    print(student.h, student.w, student.num)