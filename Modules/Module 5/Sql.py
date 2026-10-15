import sqlite3

conn = sqlite3.connect("school.db") # opens school.db, or creates it
cur = conn.cursor() # the cursor runs SQL commands

# ---------- Create the table ----------
cur.execute("DROP TABLE IF EXISTS students")

cur.execute("""
CREATE TABLE students
( id INT NOT NULL,
name VARCHAR(30) NOT NULL,
age INT,
major VARCHAR(20),
credits INT,
email VARCHAR(40),
PRIMARY KEY (id) )
""")
# ---------- Add rows ----------
cur.execute("""
INSERT INTO students
VALUES (1, 'Maya', 18, 'Biology', 15, 'maya@example.edu')
""")

students = [
(2, "Leo", 21, "History", 45, None),
(3, "Ana", 19, "Biology", 30, "ana@example.edu"),
(4, "Sam", 22, "Math", 60, None),
(5, "Priya", 20, "Computer Science", 40, "priya@example.edu"),
(6, "Omar", 18, "Math", 12, "omar@example.edu"),
(7, "Mia", 23, "History", 75, "mia@example.edu"),
(8, "Jon", 19, "Computer Science", 28, None),
]
query = "INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)"
cur.executemany(query, students)

conn.commit() # save the changes to the file
print("Students added.")
# ---------- Read rows ----------
print("\nEvery student:")
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

print("\nStudents aged 20 or older:")
cur.execute("SELECT name, age FROM students WHERE age >= 20")
for row in cur.fetchall():
    print(row)

print("Table created.")


conn.close()
print("\nDone.")
