class Student:

    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
       return self.grade
class Course:

    def __init__(self, name,max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_students(self,student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.grade
        return value / len(self.students)


s1 = Student("Rahul",25,96)
s2 = Student("Afam",25,98)
s3 = Student("Fazil",22,99)

course = Course("Science",2)
course.add_students(s1)
course.add_students(s2)


print(course.add_students(s3))
print(course.get_average_grade())