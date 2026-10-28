import pandas as pd
import os

folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(folder, "students.csv")

data = pd.read_csv(csv_path)

# Calculate average marks
data["average"] = data[
    ["math_score", "reading_score", "writing_score"]
].mean(axis=1)

# Display average marks
print("STUDENT AVERAGE MARKS")
print(data[["gender", "math_score", "reading_score",
            "writing_score", "average"]])

# Overall subject averages
print("\nSUBJECT-WISE AVERAGE")
print(data[["math_score", "reading_score",
            "writing_score"]].mean())

# Highest average
print("\nHIGHEST AVERAGE:")
print(data["average"].max())

# Lowest average
print("\nLOWEST AVERAGE:")
print(data["average"].min())
# Gender-wise performance analysis
print("\nGENDER-WISE PERFORMANCE")

gender_analysis = data.groupby("gender")[
    ["math_score", "reading_score", "writing_score", "average"]
].mean()

print(gender_analysis)

# Find better performing group in this sample
print("\nAVERAGE SCORE COMPARISON")

if gender_analysis.loc["female", "average"] > gender_analysis.loc["male", "average"]:
    print("Female students have a higher average score in this sample.")
else:
    print("Male students have a higher average score in this sample.")
    