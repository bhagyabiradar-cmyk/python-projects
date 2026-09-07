print("🎯 Welcome to the Python Quiz Game!")
print("-----------------------------------")

score = 0

# Question 1
print("\n1. Which language are we learning?")
print("A. Java")
print("B. Python")
print("C. C++")
print("D. HTML")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is B.")

# Question 2
print("\n2. Which symbol is used for comments in Python?")
print("A. //")
print("B. <!-- -->")
print("C. #")
print("D. **")

answer = input("Enter your answer: ").upper()

if answer == "C":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is C.")

# Question 3
print("\n3. Which function is used to display output?")
print("A. input()")
print("B. print()")
print("C. display()")
print("D. output()")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is B.")

# Question 4
print("\n4. Which data type stores True or False?")
print("A. String")
print("B. Integer")
print("C. Boolean")
print("D. Float")

answer = input("Enter your answer: ").upper()

if answer == "C":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is C.")

# Question 5
print("\n5. Which keyword is used to create a function?")
print("A. function")
print("B. define")
print("C. def")
print("D. fun")

answer = input("Enter your answer: ").upper()

if answer == "C":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is C.")

# Final Score
print("\n-----------------------------------")
print("🏆 Quiz Completed!")
print("Your score:", score, "/ 5")

if score == 5:
    print("🌟 Excellent! Perfect score!")
elif score >= 3:
    print("👍 Good job!")
else:
    print("📚 Keep practicing!")

print("-----------------------------------")