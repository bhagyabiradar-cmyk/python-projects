students = {
    "Bhagya": 88,
    "Rahul": 76,
    "Anu": 92,
    "Priya": 85,
    "Sneha": 95,
    "Kiran": 79
}

# Sort students by marks
sorted_students = sorted(
    students.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Top 3 Students:")

for name, marks in sorted_students[:3]:
    print(name, "-", marks)