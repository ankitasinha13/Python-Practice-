def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return average, grade


name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average, grade = calculate_grade(marks)

print("\n--- Student Result ---")
print("Name:", name)
print("Marks:", marks)
print("Average:", round(average, 2))
print("Grade:", grade)

if grade == "F":
    print("Result: Fail")
else:
    print("Result: Pass")
