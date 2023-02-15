class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"Math": 0, "Science": 0, "Chinese":0, "English":0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"Student:{self.name}\nStudent ID: {self.student_id}\n\nGrades: ")

        for course in self.grades:
            print(f"{course}: {self.grades[course]}")

Student1 = Student("Adam", "10001")
Student1.set_grade("Math", 100)
Student1.set_grade("Science", 88)
Student1.set_grade("English", 78)
Student1.set_grade("Chinese", 98)

Student1.print_grades()