# Student Management System

A simple command-line Student Management System built with **Python** and **SQLite**, demonstrating full **CRUD** (Create, Read, Update, Delete) operations.

## Features

- ➕ Add a new student
- ✏️ Update student details
- 🗑️ Delete a student
- 🔍 Search for a student by ID or name
- 📋 View all students
- 💾 Persistent storage using SQLite (`students.db`)

## Project Structure

```
student_management_system/
├── main.py        # CLI entry point / menu system
├── crud.py        # CRUD operations (add, get, update, delete, search)
├── database.py    # SQLite connection & schema setup
└── README.md
```

## Requirements

- Python 3.7+
- No external dependencies — uses the built-in `sqlite3` module.

## How to Run

```bash
python main.py
```

On first run, a `students.db` SQLite database file will be created automatically in the same directory, with a `students` table defined as:

| Column  | Type    | Notes                     |
|---------|---------|---------------------------|
| id      | INTEGER | Primary key, auto-increment |
| name    | TEXT    | Required                  |
| age     | INTEGER | Required                  |
| email   | TEXT    | Unique                    |
| course  | TEXT    | Required                  |
| grade   | TEXT    | Optional                  |

## Menu Options

```
1. Add Student
2. Update Student
3. Delete Student
4. Search Student (by ID or Name)
5. View All Students
6. Exit
```

## Example Usage

```
Enter your choice (1-6): 1

============ ADD NEW STUDENT ============
Name: Alice Johnson
Age: 20
Email: alice@example.com
Course: Computer Science
Grade (optional): A

Student added successfully with ID: 1
```

## Extending the Project

Some ideas to build on this foundation:
- Add input validation (e.g., email format checking)
- Export student records to CSV/Excel
- Add a GUI using Tkinter or a web interface using Flask/FastAPI
- Add authentication for multiple users/admins
- Add course/grade statistics and reporting

## License

Free to use and modify for learning purposes.
