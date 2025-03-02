import mysql.connector


# MySQL Connection Function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Change if MySQL is running on another server
        user="root",  # Replace with your MySQL username
        password="YASociety@104",  # Replace with your MySQL password
        database="brijmysql"
    )


# Function to Insert Data into MySQL
def insert_student_data(name, class_for_tution, mobile, subject):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO students (student_name, class, mobile_number, subject) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, class_for_tution, mobile, subject))
    conn.commit()
    cursor.close()
    conn.close()