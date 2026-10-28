# Create and write file
with open("student.txt", "w") as file:
    file.write("Name: Subh\n")
    file.write("College: IIT Patna\n")
    file.write("CGPA: 9.0\n")

# Read file
with open("student.txt", "r") as file:
    data = file.read()
    print(data)

# Append new information
with open("student.txt", "a") as file:
    file.write("Course: Computer Science\n")
    