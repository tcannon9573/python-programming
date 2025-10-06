class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Major: {self.major}"
    

class UndergraduateStudent(Student):
    pass


if __name__ == "__main__":
    student = Student("Jack", "U1010", "Computer Science")
    print (student)

    undergrad = UndergraduateStudent("Alice", "R454", "Physics")
    print (undergrad)
