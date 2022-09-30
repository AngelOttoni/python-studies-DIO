class Student:
    school = "DIO"

    def __init__(self, name, enrollment_number):
        self.name = name
        self.enrollment_number = enrollment_number

    def __str__(self) -> str:
        return f"{self.name} - {self.enrollment_number} - {self.school}"


def show_values(*objs):
    for obj in objs:
        print(obj)


student_1 = Student("Guilherme", 1)
student_2 = Student("Giovanna", 2)
show_values(student_1, student_2)

Student.school = "Python"
student_3 = Student("Chappie", 3)
show_values(student_1, student_2, student_3)
