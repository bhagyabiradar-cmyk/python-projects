total = 0

for i in range(5):
    expense = float(input("Enter expense: ₹"))
    total += expense

print("Total expense: ₹", total)

if total > 1000:
    print("You spent more than ₹1000")
else:
    print("You are within ₹1000")