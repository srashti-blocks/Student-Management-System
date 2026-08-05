
import sqlite3
from database import get_connection


class StudentNotFoundError(Exception):
    """Raised when a student record cannot be found."""
    pass


def add_student(name: str, age: int, email: str, course: str, grade: str = "") -> int:
    """Insert a new student record. Returns the new student's ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                """INSERT INTO students (name, age, email, course, grade)
                   VALUES (?, ?, ?, ?, ?)""",
                (name, age, email, course, grade),
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Could not add student: {e}")


def get_all_students():
    """Return a list of all students, ordered by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students ORDER BY id")
        return cursor.fetchall()


def get_student_by_id(student_id: int):
    """Return a single student record by ID, or None if not found."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        return cursor.fetchone()


def search_students_by_name(name: str):
    """Return all students whose name contains the given substring (case-insensitive)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ? ORDER BY name",
            (f"%{name}%",),
        )
        return cursor.fetchall()


def update_student(student_id: int, **fields) -> bool:
    """
    Update one or more fields of a student record.
    Example: update_student(3, age=21, course="Data Science")
    Returns True if a row was updated, False if the student was not found.
    """
    if not fields:
        raise ValueError("No fields provided to update.")

    allowed_fields = {"name", "age", "email", "course", "grade"}
    invalid = set(fields) - allowed_fields
    if invalid:
        raise ValueError(f"Invalid field(s): {', '.join(invalid)}")

    set_clause = ", ".join(f"{key} = ?" for key in fields)
    values = list(fields.values()) + [student_id]

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE students SET {set_clause} WHERE id = ?", values
        )
        conn.commit()
        return cursor.rowcount > 0


def delete_student(student_id: int) -> bool:
    """Delete a student record by ID. Returns True if a row was deleted."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        return cursor.rowcount > 0
