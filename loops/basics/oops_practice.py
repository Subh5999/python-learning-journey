class Student:

    def __init__(self, name, branch, cgpa):
        self.name = name
        self.branch = branch
        self.cgpa = cgpa

    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("CGPA:", self.cgpa)


student1 = Student("Subh", "Computer Science", 9.0)
student2 = Student("Rahul", "Data Science", 8.5)

student1.display()
print()

student2.display()