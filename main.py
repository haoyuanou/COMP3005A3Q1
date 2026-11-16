import psycopg2
from psycopg2 import Error

DB_CONFIG = {
    "dbname": "comp3005_a3", 
    "user": "postgres",      
    "password": "12345678", 
    "host": "localhost",
    "port": "5432"
}

def connect():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def getAllStudents():
    # Retrieves and displays all records from the students table
    conn = connect()

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students ORDER BY student_id ASC;")
            records = cursor.fetchall()

            print("\n--- All Students ---")
            for r in records:
                print(f"ID: {r[0]}, Name: {r[1]} {r[2]}, Email: {r[3]}, Enrolled: {r[4]}")
            cursor.close()
        except Error as e:
            print(f"Error reading data: {e}")
        finally:
            conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    #Inserts a new student record into the students table

    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            insert_query = """INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"""
            cursor.execute(insert_query, (first_name, last_name, email, enrollment_date))
            conn.commit()

            print(f"\nSuccess: Student {first_name} {last_name} added.")
            cursor.close()
        except Error as e:
            print(f"Error inserting data: {e}")
        finally:
            conn.close()

def updateStudentEmail(student_id, new_email):
    #Updates the email address for a student with the specified student_id

    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            update_query = "UPDATE students SET email = %s WHERE student_id = %s"
            cursor.execute(update_query, (new_email, student_id))
            conn.commit()

            print(f"\nSuccess: Email for student ID {student_id} updated to {new_email}.")
            cursor.close()
        except Error as e:
            print(f"Error updating data: {e}")
        finally:
            conn.close()

def deleteStudent(student_id):
    #Deletes the record of the student with the specified student_id

    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            delete_query = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(delete_query, (student_id,))
            conn.commit()
            
            print(f"\nSuccess: Student with ID {student_id} deleted.")
            cursor.close()
        except Error as e:
            print(f"Error deleting data: {e}")
        finally:
            conn.close()

# Testing Demo
if __name__ == "__main__":
    # 1. Print all students
    getAllStudents()
    input("\nPress Enter to ccontinue.")
    
    # 2. Add a new student
    addStudent('Kylian', 'Mbappe', 'kyky@gmail.com', '2024-09-01')
    getAllStudents()
    input("\nPress Enter to ccontinue.")
    
    # 3. Update student email
    updateStudentEmail(4, 'kmbappe10@gmail.com')
    getAllStudents()
    input("\nPress Enter to ccontinue.")
    
    # 4. Delete the student
    deleteStudent(4)
    getAllStudents()
    print("\nDone!")