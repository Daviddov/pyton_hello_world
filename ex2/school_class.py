from student_class import Student
class School:
    def __init__(self):
        self.students = []
    def add_student(self, st):
        for student in self.students:
            if student.id == st.id:
                print("Student already added.")
                return
        self.students.append(st)

    def print_students_data(self):
        for student in self.students:
            student.print_data()


if __name__ == "__main__":
    school = School()
    st = Student("David", 1, 2)
    st1 = Student("David", 2, 2)
    st.add_grade(9)
    st.add_grade(5)
    st1.add_grade(6)
    st1.add_grade(11)
    school.add_student(st)
    school.add_student(st1)
    school.students.sort(key=lambda s: s.grades)
    school.print_students_data()
