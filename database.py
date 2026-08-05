
import sqlite3
from contextlib import contextmanager

DB_NAME = "students.db"


def initialize_db():
    """Create the students table if it doesn't already exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT UNIQUE,
                course TEXT NOT NULL,
                grade TEXT
            )
        """)
        conn.commit()


@contextmanager
def get_connection():
    """Context manager that yields a SQLite connection and closes it safely."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # allows dict-like access to rows
    try:
        yield conn
    finally:
        conn.close()
