numbers = [10, 20, 30, 20, 40, 50, 10, 60, 30, 70]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Original List:")
print(numbers)

print("\nDuplicate Values:")
print(duplicates)

print("\nNumber of Duplicates:", len(duplicates))