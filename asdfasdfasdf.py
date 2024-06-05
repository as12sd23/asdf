class Student:
    def __init__(self, name,score):
        self.name = name
        self.score = score

class StudentList:
    def __init__(self):

        self.students = []

    def append(self, student):
        self.students.append(student)
    def get_aver(self):
        return sum([i.score for i in self.students]) / len(self.students)
    def get_first(self):
        return [self.students[i] for i in range(0, len(self.students)) if self.students[i].score == max([i.score for i in self.students])]
    def get_last(self):
        return min([i.score for i in self.students])
students = StudentList()
students.append(Student("구름", 100))
students.append(Student("별", 49))
students.append(Student("초코", 81))
students.append(Student("아지", 90))

print(students.get_aver())

a = students.get_first()
for i in a:
    print(i.name)
print(students.get_last().name)
