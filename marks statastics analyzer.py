# Marks Statistics Analyzer

marks = [78, 85, 92, 67, 88, 74, 95, 81, 69, 90]

print("===== MARKS ANALYZER =====")

print("Marks:", marks)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nTotal Marks:", total)
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

print("\nStudents who scored above average:")

for mark in marks:
    if mark > average:
        print(mark)

print("\nGrade Analysis:")

for mark in marks:
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "D"

    print(mark, "->", grade)