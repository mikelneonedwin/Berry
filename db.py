import sqlite3

DB_NAME = "app.db"

def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DB_NAME)

def create_schema():
    """Create the students table if it doesn't already exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            matric TEXT UNIQUE NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("Schema created successfully.")

def add_student(name, matric):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, matric) VALUES (?, ?)", (name, matric))
    conn.commit()
    conn.close()

def get_student_by_matric(matric):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, matric FROM students WHERE matric = ?", (matric,))
    student = cursor.fetchone()
    conn.close()
    return student


# Example usage:
if __name__ == "__main__":
    create_schema()
    add_student("Alice Johnson", "20/BCS/PT/009TR")
    add_student("Bob Smith", "22/SC/CO/1149")

    student = get_student_by_matric("20/BCS/PT/009TR")
    if student:
        print("Student found:", student)
    else:
        print("No student found with that matric number.")
