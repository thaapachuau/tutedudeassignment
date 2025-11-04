# 1. Create a dictionary where student names are keys and their marks are values.
student_marks = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 72,
    "Diana": 91,
    "Eve": 65
}

# 2. Ask the user to input a student's name.
student_name = input("Enter the student's name: ")

# 3. Retrieve and display the corresponding marks, or display an appropriate message if not found.
if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"{student_name}'s marks: {marks}")
else:
    # 4. If the student’s name is not found, display an appropriate message.
    print(f"Student '{student_name}' not found in the records.")