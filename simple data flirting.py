students = {
    "Bhagya": 85,
    "Rahul": 62,
    "Anu": 91,
    "Priya": 48,
    "Kiran": 76
}

print("Students who scored 70 or above:")

for name, marks in students.items():
    if marks >= 70:
        print(name, ":", marks)