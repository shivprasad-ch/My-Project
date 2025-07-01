import psycopg2

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="student_db",
    user="postgres",
    password="shivprasad1999"
)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    marks FLOAT
)
""")
conn.commit()

def add_student():
    while True:
        roll_no = input("Enter Roll Number (only digits): ")
        if not roll_no.isdigit():
            print("Invalid Roll Number. Example: 1")
            continue
        break

    while True:
        name = input("Enter Name (letters only): ")
        if not name.replace(" ", "").isalpha():
            print("Invalid Name. Example: Rahul Sharma")
            continue
        break

    while True:
        age = input("Enter Age (1–100): ")
        if not age.isdigit():
            print("Age must be a number. Example: 20")
            continue
        age = int(age)
        if age < 1 or age > 100:
            print("Age must be between 1 and 100.")
            continue
        break

    while True:
        marks = input("Enter Marks (0–100): ")
        try:
            marks = float(marks)
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100. Example: 88.5")
                continue
            break
        except ValueError:
            print("Marks must be a number. Example: 75.5")

    try:
        cursor.execute(
            "INSERT INTO students (roll_no, name, age, marks) VALUES (%s, %s, %s, %s)",
            (roll_no, name, age, marks)
        )
        conn.commit()
        print("Student added successfully.\n")
    except psycopg2.IntegrityError:
        conn.rollback()
        print(" Error: Roll Number already exists.\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("No students found.\n")
        return
    print("\n--- All Student Records ---")
    for row in rows:
        print(f"Roll No: {row[0]}, Name: {row[1]}, Age: {row[2]}, Marks: {row[3]}")
    print()

def search_student():
    roll_no = input("Enter Roll Number to search: ")
    cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    student = cursor.fetchone()
    if student:
        print(f"\n Found Student:\nRoll No: {student[0]}, Name: {student[1]}, Age: {student[2]}, Marks: {student[3]}\n")
    else:
        print("Student not found.\n")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    student = cursor.fetchone()
    if student:
        cursor.execute("DELETE FROM students WHERE roll_no = %s", (roll_no,))
        conn.commit()
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")

# Main menu
while True:
    print("===== Student Record Menu =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll Number")
    print("4. Delete Student by Roll Number")
    print("5. Exit")
    choice = input("Enter your choice (1–5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        confirm = input("Are you sure you want to exit? (yes/no): ").lower()
        if confirm == 'yes':
            print("Exiting the application.\nTHANK YOU! 🙏😊")
            break
        else:
            print("Returning to main menu.\n")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")

cursor.close()
conn.close()
