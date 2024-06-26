import streamlit as st
import mysql.connector
from mysql.connector import Error
import datetime

# Cache to store deleted courses
deleted_courses_cache = []

# Database connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='AAKash44',
            database='eduschema'
        )
        if connection.is_connected():
            print("Connected to the database")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def add_course(connection):
    with st.form("add_course"):
        course_name = st.text_input("Course Name")
        course_description = st.text_area("Course Description")
        course_start_date = st.date_input("Course Start Date")
        course_end_date = st.date_input("Course End Date")
        course_category = st.text_input("Course Category")
        submit = st.form_submit_button("Add Course")
        if submit:
            cursor = connection.cursor()
            query = """
            INSERT INTO Courses (course_name, course_description, course_start_date, course_end_date, course_category)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (course_name, course_description, course_start_date, course_end_date, course_category))
            connection.commit()
            st.success("Course added successfully.")

def update_course(connection):
    with st.form("update_course"):
        course_id = st.number_input("Course ID", min_value=1)
        course_name = st.text_input("New Course Name")
        course_description = st.text_area("New Course Description")
        course_start_date = st.date_input("New Course Start Date")
        course_end_date = st.date_input("New Course End Date")
        course_category = st.text_input("New Course Category")
        submit = st.form_submit_button("Update Course")
        if submit:
            cursor = connection.cursor()
            query = """
            UPDATE Courses
            SET course_name = %s, course_description = %s, course_start_date = %s, course_end_date = %s, course_category = %s
            WHERE course_id = %s
            """
            cursor.execute(query, (course_name, course_description, course_start_date, course_end_date, course_category, course_id))
            connection.commit()
            st.success("Course updated successfully.")

def search_courses(connection):
    with st.form("search_courses"):
        search_term = st.text_input("Search Term")
        submit = st.form_submit_button("Search Courses")
        if submit:
            cursor = connection.cursor()
            query = "SELECT * FROM Courses WHERE course_name LIKE %s"
            cursor.execute(query, ('%' + search_term + '%',))
            results = cursor.fetchall()
            for row in results:
                if st.button(f"Course: {row[1]}, Start Date: {row[3]}"):  # Button representation
                    st.table([row])  # Display the course details in a table if button is clicked

def sort_courses(connection):
    sort_by = st.selectbox("Sort by", ["course_name", "course_start_date", "course_end_date"])
    cursor = connection.cursor()
    query = f"SELECT * FROM Courses ORDER BY {sort_by}"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        st.table([row])  # Display each row as a table

def remove_course(connection):
    with st.form("remove_course"):
        course_id = st.number_input("Course ID to Remove", min_value=1)
        submit = st.form_submit_button("Remove Course")
        if submit:
            cursor = connection.cursor()
            query = "SELECT * FROM Courses WHERE course_id = %s"
            cursor.execute(query, (course_id,))
            course = cursor.fetchone()
            if course:
                deleted_courses_cache.append(course)
                query = "DELETE FROM Courses WHERE course_id = %s"
                cursor.execute(query, (course_id,))
                connection.commit()
                st.success("Course removed successfully.")
            else:
                st.error("Course ID not found.")

def view_deleted_courses():
    st.subheader("Deleted Courses")
    for course in deleted_courses_cache:
        st.table([course])  # Display each deleted course as a table

def add_instructor(connection):
    with st.form("add_instructor"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone_number = st.text_input("Phone Number")
        profile_description = st.text_area("Profile Description")
        submit = st.form_submit_button("Add Instructor")
        if submit:
            cursor = connection.cursor()
            query = """
            INSERT INTO Instructors (first_name, last_name, email, phone_number, profile_description)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (first_name, last_name, email, phone_number, profile_description))
            connection.commit()
            st.success("Instructor added successfully.")

def assign_instructor_to_course(connection):
    with st.form("assign_instructor"):
        course_id = st.number_input("Course ID", min_value=1)
        instructor_id = st.number_input("Instructor ID", min_value=1)
        submit = st.form_submit_button("Assign Instructor to Course")
        if submit:
            cursor = connection.cursor()
            query = "INSERT INTO Course_Instructors (course_id, instructor_id) VALUES (%s, %s)"
            cursor.execute(query, (course_id, instructor_id))
            connection.commit()
            st.success("Instructor assigned to course successfully.")

def view_instructors_assigned(connection):
    cursor = connection.cursor()
    query = """
    SELECT Courses.course_name, Instructors.first_name, Instructors.last_name
    FROM Courses
    JOIN Course_Instructors ON Courses.course_id = Course_Instructors.course_id
    JOIN Instructors ON Course_Instructors.instructor_id = Instructors.instructor_id
    ORDER BY Courses.course_name
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        if st.button(f"Course: {row[0]}, Instructor: {row[1]} {row[2]}"):  # Button representation
            st.table([row])  # Display the course-instructor details in a table if button is clicked

def enroll_student(connection):
    with st.form("enroll_student"):
        student_id = st.number_input("Student ID", min_value=1)
        course_id = st.number_input("Course ID", min_value=1)
        enrollment_date = st.date_input("Enrollment Date")
        submit = st.form_submit_button("Enroll Student")
        if submit:
            cursor = connection.cursor()
            query = """
            INSERT INTO Enrollments (student_id, course_id, enrollment_date, progress)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (student_id, course_id, enrollment_date, 0.00))
            connection.commit()
            st.success("Student enrolled successfully.")

def track_progress(connection):
    student_id = st.number_input("Enter Your Enrollment ID", min_value=1)
    cursor = connection.cursor()

    query_enrollments = """
    SELECT enrollment_id, course_id, progress
    FROM Enrollments
    WHERE student_id = %s
    """
    cursor.execute(query_enrollments, (student_id,))
    enrollments = cursor.fetchall()

    if enrollments:
        st.subheader("Your Progress")
        for enrollment in enrollments:
            st.write(f"Course ID: {enrollment[1]}")

        st.subheader("Assessments and Grades")
        for enrollment in enrollments:
            enrollment_id = enrollment[0]
            query_grades = """
            SELECT Assessments.assessment_name, Grades.score
            FROM Grades
            JOIN Assessments ON Grades.assessment_id = Assessments.assessment_id
            WHERE Grades.enrollment_id = %s
            """
            cursor.execute(query_grades, (enrollment_id,))
            grades = cursor.fetchall()

            if grades:
                st.write(f"Course ID: {enrollment[1]}")
                for grade in grades:
                    st.write(f"Assessment: {grade[0]}, Score: {grade[1]}")

    else:
        st.warning("No enrollments found for this Enrollment ID.")

def add_assessment(connection):
    with st.form("add_assessment"):
        course_id = st.number_input("Course ID", min_value=1)
        assessment_name = st.text_input("Assessment Name")
        assessment_type = st.selectbox("Assessment Type", ["Quiz", "Assignment", "Exam", "Project"])
        max_score = st.number_input("Maximum Score", min_value=0.0)
        submit = st.form_submit_button("Add Assessment")
        if submit:
            cursor = connection.cursor()
            query = """
            INSERT INTO Assessments (course_id, assessment_name, assessment_type, max_score)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (course_id, assessment_name, assessment_type, max_score))
            connection.commit()
            st.success("Assessment added successfully.")

def input_grade(connection):
    with st.form("input_grade"):
        enrollment_id = st.number_input("Enrollment ID", min_value=1)
        assessment_id = st.number_input("Assessment ID", min_value=1)
        score = st.number_input("Score", min_value=0.0)
        submit = st.form_submit_button("Input Grade")
        if submit:
            cursor = connection.cursor()
            query = """
            INSERT INTO Grades (enrollment_id, assessment_id, score)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (enrollment_id, assessment_id, score))
            connection.commit()
            st.success("Grade input successfully.")

def view_grades(connection):
    with st.form("view_grades"):
        enrollment_id = st.number_input("Enrollment ID to view grades", min_value=1)
        submit = st.form_submit_button("View Grades")
        if submit:
            cursor = connection.cursor()
            query = """
            SELECT Assessments.assessment_name, Grades.score
            FROM Grades
            JOIN Assessments ON Grades.assessment_id = Assessments.assessment_id
            WHERE Grades.enrollment_id = %s
            """
            cursor.execute(query, (enrollment_id,))
            grades = cursor.fetchall()
            for row in grades:
                st.write(f"Assessment: {row[0]}, Score: {row[1]}")

def app():
    st.title("EDU SCHEMA")
    connection = create_connection()
    
    if connection:
        st.sidebar.title("Navigation")
        options = st.sidebar.radio("Select an option", [
            "Course Management", 
            "Instructor Management", 
            "Student Management", 
            "Assessment Management", 
            "Grade Management"
        ])

        if options == "Course Management":
            st.header("Course Management")
            add_course(connection)
            update_course(connection)
            remove_course(connection)
            search_courses(connection)
            sort_courses(connection)
            view_deleted_courses()

        elif options == "Instructor Management":
            st.header("Instructor Management")
            add_instructor(connection)
            assign_instructor_to_course(connection)
            view_instructors_assigned(connection)

        elif options == "Student Management":
            st.header("Student Management")
            enroll_student(connection)
            track_progress(connection)

        elif options == "Assessment Management":
            st.header("Assessment Management")
            add_assessment(connection)

        elif options == "Grade Management":
            st.header("Grade Management")
            input_grade(connection)
            view_grades(connection)
    else:
        st.error("Failed to connect to the database.")

if __name__ == "__main__":
    app()
