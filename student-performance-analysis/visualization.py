print("Visualization file is running!")

import pandas as pd
import matplotlib.pyplot as plt
import os

folder = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(folder, "students.csv"))

print("CSV loaded successfully!")

subjects = ["math_score", "reading_score", "writing_score"]
averages = data[subjects].mean()

print(averages)

averages.plot(kind="bar")
plt.title("Average Marks by Subject")


print("Graph code completed!")
plt.tight_layout()

output_path = os.path.join(folder, "subject_average.png")
plt.savefig(output_path)

print("Graph saved successfully!")
# Calculate average marks for each student
data["average"] = data[
    ["math_score", "reading_score", "writing_score"]
].mean(axis=1)

# Create student-wise bar chart
plt.figure(figsize=(10, 5))

plt.bar(range(1, len(data) + 1), data["average"])

plt.title("Student-wise Average Marks")
plt.xlabel("Student Number")
plt.ylabel("Average Marks")

plt.tight_layout()

# Save second graph
output_path = os.path.join(folder, "student_average.png")
plt.savefig(output_path)

print("Student-wise graph saved successfully!")