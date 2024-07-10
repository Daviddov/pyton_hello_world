class Student:
    def __init__(self, name, id, max_grades_size):
        self.name = name
        self.id = id
        self.grades = []
        self.max_grades_size = max_grades_size

    def print_data(self):
        print(self.name, self.id)
        for grade in self.grades:
            print(grade)

    def add_grade(self, grade):
        if len(self.grades) < self.max_grades_size :
            self.grades.append(grade)
        else:
            print("no place")


    def get_avg(self):
        sum = 0
        for grade in self.grades:
            sum += grade
        return sum / len(self.grades)

    def __add__(self, other):
        name = self.name + other.name
        id = self.id + other.id
        if self.get_avg() > other.get_avg():
            grades = self.grades
        else:
            grades = other.grades
        s = Student(name, id, len(grades))
        for grade in grades:
            s.add_grade(grade)
        return s

    def __gt__(self, other):
        if max(self.grades) > max(other.grades):
            return True
        else:
            return False

    def __str__(self):
        return f"name: {self.name}, id: {self.id}, grades: {self.grades}"

if __name__ == "__main__":
    st = Student("David", 1, 2)
    st2 = Student("David", 2, 2)

    st.add_grade(3)
    st.add_grade(5)
    st2.add_grade(6)
    st3 = st + st2 + st
    li = [st3, st2,st]
    li.sort()#by gt
    li.sort(key=lambda x: x.id)#by val from lamde
    for i in li:
        print(i)
# print(st>st2)
    # print(st3)
    # st.print_data()
    # print(st.get_avg())