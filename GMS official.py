# Data structure: List of lists where each list contains [student_name, assignment_mark, test_mark, exam_mark]
students = [
    ["Alice", 85, 90, 78],
    ["Bob", 92, 88, 79],
    ["Charlie", 95, 91, 89],
    ["David", 76, 84, 90],
    ["Eva", 88, 92, 85],
    ["Frank", 80, 83, 88],
    ["Grace", 91, 89, 95],
    ["Henry", 85, 87, 90],
    ["Ivy", 93, 94, 91],
    ["Jack", 77, 79, 85]
]

def display_students():
    print("\nStudents:")
    print(f"{'Name':<10} {'Assignment Mark':<16} {'Test Mark':<10} {'Exam Mark':<10}")
    print("="*48)
    for student in students:
        name, assignment, test, exam = student
        print(f"{name:<10} {assignment:<16} {test:<10} {exam:<10}")
    print()

def add_student():
    name = input("Enter student's name: ")
    assignment_mark = int(input("Enter assignment mark: "))
    test_mark = int(input("Enter test mark: "))
    exam_mark = int(input("Enter exam mark: "))
    students.append([name, assignment_mark, test_mark, exam_mark])
    print(f"Student {name} added.\n")

def remove_student():
    name = input("Enter student's name to remove: ")
    global students
    students = [student for student in students if student[0] != name]
    print(f"Student {name} removed.\n")

def update_grades():
    name = input("Enter student's name to update grades: ")
    for student in students:
        if student[0] == name:
            new_grades = input("Enter new grades separated by commas: ")
            new_grades_list = [int(grade.strip()) for grade in new_grades.split(',')]
            student[1:] = new_grades_list
            print(f"Grades for {name} updated.\n")
            return
    print(f"Student {name} not found.\n")

def calculate_average_grades():
    averages = {}
    for student in students:
        name, assignment, test, exam = student
        averages[name] = (assignment + test + exam) / 3
    return averages

def display_top_achievers():
    averages = calculate_average_grades()
    sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_students[:3]
    print("Top 3 Achievers:")
    for name, avg in top_3:
        print(f"Name: {name}, Average Grade: {avg:.2f}")
    print()

def prompt_and_print_student_record():
    name = input("Enter student's name: ")
    for student in students:
        if student[0] == name:
            print(f"Name: {student[0]}, Assignment Mark: {student[1]}, Test Mark: {student[2]}, Exam Mark: {student[3]}\n")
            return
    print(f"Student {name} not found.\n")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Students")
        print("2. Display Students")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            manage_students_menu()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

def manage_students_menu():
    while True:
        print("\nManage Students Menu")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Grades")
        print("4. Display Top 3 Achievers")
        print("5. Search Student Record")
        print("6. Back to Main Menu")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            update_grades()
        elif choice == '4':
            display_top_achievers()
        elif choice == '5':
            prompt_and_print_student_record()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main_menu()
