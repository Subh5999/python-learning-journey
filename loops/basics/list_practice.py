marks = [85, 90, 78, 92, 88]

total = 0

for mark in marks:
    print(mark)
    total = total + mark

print("Total Marks:", total)
print("Average Marks:", total / len(marks))
for mark in marks:
    if mark >= 80:
        print(mark)