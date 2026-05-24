class Students:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = int(age)
        self.marks = float(marks)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        elif self.marks >= 50:
            return "E"
        else:
            return "F"

    def display_stuinfo(self):
        print("Name", self.name)
        print("Age", self.age)
        print("Marks", self.marks)
        print("Grade", self.grade)

name = input("Enter Name: ")
age = input("Enter Age: ")
marks = input("Enter Marks: ")

student1 = Students(name, age, marks)
student1.display_stuinfo()

name = input("Enter Name: ")
age = input("Enter Age: ")
marks = input("Enter Marks: ")

student2 = Students(name, age, marks)
student2.display_stuinfo()
