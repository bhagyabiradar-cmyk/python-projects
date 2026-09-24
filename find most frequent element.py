numbers = [10, 20, 10, 30, 20, 10, 40, 20, 10]

most_frequent = max(set(numbers), key=numbers.count)

print("Most frequent number:", most_frequent)
print("Count:", numbers.count(most_frequent))