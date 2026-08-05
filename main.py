
from database import initialize_db
import crud


def print_header(title: str):
    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)


def print_student_row(student):
    print(
        f"ID: {student['id']:<4} | Name: {student['name']:<20} | "
        f"Age: {student['age']:<3} | Email: {student['email']:<25} | "
        f"Course: {student['course']:<15} | Grade: {student['grade']}"
    )


def print_menu():
    print_header("STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student (by ID or Name)")
    print("5. View All Students")
    print("6. Exit")


def prompt_int(prompt: str):
    """Keep asking until the user enters a valid integer."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")


def handle_add_student():
    print_header("ADD NEW STUDENT")
    name = input("Name: ").strip()
    age = prompt_int("Age: ")
    email = input("Email: ").strip()
    course = input("Course: ").strip()
    grade = input("Grade (optional): ").strip()

    if not name or not course:
        print("Name and Course are required fields. Student not added.")
        return

    try:
        new_id = crud.add_student(name, age, email, course, grade)
        print(f"\nStudent added successfully with ID: {new_id}")
    except ValueError as e:
        print(f"\nError: {e}")


def handle_update_student():
    print_header("UPDATE STUDENT")
    student_id = prompt_int("Enter Student ID to update: ")
    student = crud.get_student_by_id(student_id)

    if not student:
        print(f"No student found with ID {student_id}.")
        return

    print("\nCurrent details:")
    print_student_row(student)
    print("\nLeave a field blank to keep it unchanged.")

    updates = {}
    name = input(f"New Name [{student['name']}]: ").strip()
    age = input(f"New Age [{student['age']}]: ").strip()
    email = input(f"New Email [{student['email']}]: ").strip()
    course = input(f"New Course [{student['course']}]: ").strip()
    grade = input(f"New Grade [{student['grade']}]: ").strip()

    if name:
        updates["name"] = name
    if age:
        if age.isdigit():
            updates["age"] = int(age)
        else:
            print("Invalid age entered, skipping age update.")
    if email:
        updates["email"] = email
    if course:
        updates["course"] = course
    if grade:
        updates["grade"] = grade

    if not updates:
        print("\nNo changes made.")
        return

    try:
        success = crud.update_student(student_id, **updates)
        print("\nStudent updated successfully." if success else "\nUpdate failed.")
    except ValueError as e:
        print(f"\nError: {e}")


def handle_delete_student():
    print_header("DELETE STUDENT")
    student_id = prompt_int("Enter Student ID to delete: ")
    student = crud.get_student_by_id(student_id)

    if not student:
        print(f"No student found with ID {student_id}.")
        return

    print_student_row(student)
    confirm = input("\nAre you sure you want to delete this student? (y/n): ").strip().lower()
    if confirm == "y":
        crud.delete_student(student_id)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def handle_search_student():
    print_header("SEARCH STUDENT")
    print("1. Search by ID")
    print("2. Search by Name")
    choice = input("Choose an option (1-2): ").strip()

    if choice == "1":
        student_id = prompt_int("Enter Student ID: ")
        student = crud.get_student_by_id(student_id)
        if student:
            print_student_row(student)
        else:
            print(f"No student found with ID {student_id}.")

    elif choice == "2":
        name = input("Enter name (or part of it): ").strip()
        results = crud.search_students_by_name(name)
        if results:
            print(f"\nFound {len(results)} matching student(s):\n")
            for s in results:
                print_student_row(s)
        else:
            print("No matching students found.")
    else:
        print("Invalid option.")


def handle_view_all():
    print_header("ALL STUDENTS")
    students = crud.get_all_students()
    if not students:
        print("No students found in the database.")
        return
    for s in students:
        print_student_row(s)
    print(f"\nTotal students: {len(students)}")


def main():
    initialize_db()

    actions = {
        "1": handle_add_student,
        "2": handle_update_student,
        "3": handle_delete_student,
        "4": handle_search_student,
        "5": handle_view_all,
    }

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("\nGoodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("\nInvalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
