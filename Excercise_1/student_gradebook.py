
gradebook = {}

# Function to calculate average
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

# Function to determine letter grade
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Add new student
def add_student():
    name = input("Enter student name: ")
    if name in gradebook:
        print("Student already exists.")
    else:
        gradebook[name] = []
        print(f"{name} has been added.\n")

# Add grade to existing student
def add_grade():
    name = input("Enter student name: ")
    if name in gradebook:
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                gradebook[name].append(grade)
                print("Grade added.\n")
            else:
                print("Grade must be between 0 and 100.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    else:
        print("Student not found.\n")

# View student average and letter grade
def view_student():
    name = input("Enter student name: ")
    if name in gradebook:
        grades = gradebook[name]
        if grades:
            avg = calculate_average(grades)
            letter = get_letter_grade(avg)
            print(f"{name}'s Average: {avg:.2f} | Grade: {letter}\n")
        else:
            print("No grades recorded for this student.\n")
    else:
        print("Student not found.\n")

# Display class statistics
def display_class_stats(gradebook):
    if not gradebook:
        print("No students in class.")
        return

    highest_student = None
    highest_avg = -1
    lowest_student = None
    lowest_avg = 101
    total_avg = 0
    counted_students = 0

    for student, grades in gradebook.items():
        if not grades:
            continue  # Skip students with no grades

        avg = calculate_average(grades)
        total_avg += avg
        counted_students += 1

        if avg > highest_avg:
            highest_avg = avg
            highest_student = student

        if avg < lowest_avg:
            lowest_avg = avg
            lowest_student = student

    if counted_students == 0:
        print("No grades entered yet.")
        return

    class_avg = total_avg / counted_students

    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Performing Student: {highest_student} ({highest_avg:.2f})")
    print(f"Lowest Performing Student: {lowest_student} ({lowest_avg:.2f})")

# Main menu
def menu():
    while True:
        print("=== STUDENT GRADEBOOK MANAGER ===")
        print("1. Add new student")
        print("2. Add grade to existing student")
        print("3. View student average and letter grade")
        print("4. Display class statistics")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_student()
        elif choice == "4":
            display_class_stats()
        elif choice == "5":
            print("Exiting Gradebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the menu
menu()
