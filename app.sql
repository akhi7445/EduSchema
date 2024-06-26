CREATE DATABASE EduSchema;

USE EduSchema;

CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    course_description TEXT,
    course_start_date DATE,
    course_end_date DATE,
    course_category VARCHAR(100)
);

CREATE TABLE Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(15),
    profile_description TEXT
);

CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(15),
    enrollment_date DATE NOT NULL
);

CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    progress DECIMAL(5, 2) DEFAULT 0.00
);

CREATE TABLE Assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    assessment_name VARCHAR(255) NOT NULL,
    assessment_type VARCHAR(50) NOT NULL,
    max_score DECIMAL(5, 2) NOT NULL
);

CREATE TABLE Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    assessment_id INT NOT NULL,
    score DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id),
    FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id)
);

CREATE TABLE Course_Instructors (
    course_instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    instructor_id INT NOT NULL
);

INSERT INTO Courses (course_name, course_description, course_start_date, course_end_date, course_category) VALUES
('Introduction to SQL', 'Learn the basics of SQL.', '2024-07-01', '2024-09-01', 'Database'),
('Advanced SQL', 'Master advanced SQL concepts.', '2024-08-01', '2024-10-01', 'Database'),
('Python Programming', 'Learn Python from scratch.', '2024-07-15', '2024-09-15', 'Programming'),
('Data Structures', 'Understand data structures in computer science.', '2024-09-01', '2024-11-01', 'Computer Science'),
('Algorithms', 'Learn algorithms and problem-solving techniques.', '2024-09-15', '2024-11-15', 'Computer Science'),
('Web Development', 'Build websites using HTML, CSS, and JavaScript.', '2024-08-01', '2024-10-01', 'Web Development'),
('Machine Learning', 'Introduction to machine learning concepts and algorithms.', '2024-10-01', '2024-12-01', 'Data Science'),
('Artificial Intelligence', 'Basics of AI and its applications.', '2024-11-01', '2024-12-31', 'Data Science'),
('Database Design', 'Learn how to design and manage databases.', '2024-08-15', '2024-10-15', 'Database'),
('Operating Systems', 'Understand the fundamentals of operating systems.', '2024-09-01', '2024-11-01', 'Computer Science');

INSERT INTO Instructors (first_name, last_name, email, phone_number, profile_description) VALUES
('John', 'Doe', 'john.doe@example.com', '555-1234', 'Expert in SQL and databases.'),
('Jane', 'Smith', 'jane.smith@example.com', '555-5678', 'Experienced Python programmer.'),
('Emily', 'Jones', 'emily.jones@example.com', '555-8765', 'Specializes in data structures and algorithms.'),
('Michael', 'Brown', 'michael.brown@example.com', '555-4321', 'Web development and frontend expert.'),
('Sarah', 'Davis', 'sarah.davis@example.com', '555-1111', 'Machine learning and AI specialist.'),
('David', 'Wilson', 'david.wilson@example.com', '555-2222', 'Database design and management professional.'),
('Laura', 'Garcia', 'laura.garcia@example.com', '555-3333', 'Operating systems and computer science educator.'),
('Robert', 'Martinez', 'robert.martinez@example.com', '555-4444', 'Experienced in teaching web development.'),
('Linda', 'Hernandez', 'linda.hernandez@example.com', '555-5555', 'Expert in artificial intelligence.'),
('James', 'Lopez', 'james.lopez@example.com', '555-6666', 'Specializes in advanced SQL techniques.');

INSERT INTO Students (first_name, last_name, email, phone_number, enrollment_date) VALUES
('Alice', 'Johnson', 'alice.johnson@example.com', '555-7777', '2024-06-01'),
('Bob', 'Williams', 'bob.williams@example.com', '555-8888', '2024-06-02'),
('Charlie', 'Brown', 'charlie.brown@example.com', '555-9999', '2024-06-03'),
('Diana', 'Lee', 'diana.lee@example.com', '555-0000', '2024-06-04'),
('Ethan', 'Moore', 'ethan.moore@example.com', '555-1010', '2024-06-05'),
('Fiona', 'Taylor', 'fiona.taylor@example.com', '555-2020', '2024-06-06'),
('George', 'Anderson', 'george.anderson@example.com', '555-3030', '2024-06-07'),
('Hannah', 'Thomas', 'hannah.thomas@example.com', '555-4040', '2024-06-08'),
('Isaac', 'Jackson', 'isaac.jackson@example.com', '555-5050', '2024-06-09'),
('Julia', 'White', 'julia.white@example.com', '555-6060', '2024-06-10');

INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date, progress) VALUES
(1, 1, 1, '2024-06-15', 0.00),
(2, 2, 2, '2024-06-16', 0.00),
(3, 3, 3, '2024-06-17', 0.00),
(4, 4, 4, '2024-06-18', 0.00),
(5, 5, 5, '2024-06-19', 0.00),
(6, 6, 6, '2024-06-20', 0.00),
(7, 7, 7, '2024-06-21', 0.00),
(8, 8, 8, '2024-06-22', 0.00),
(9, 9, 9, '2024-06-23', 0.00),
(10, 10, 10, '2024-06-24', 0.00);

INSERT INTO Assessments (course_id, assessment_name, assessment_type, max_score) VALUES
(1, 'Quiz 1', 'Quiz', 10.00),
(2, 'Assignment 1', 'Assignment', 20.00),
(3, 'Midterm Exam', 'Exam', 50.00),
(4, 'Quiz 2', 'Quiz', 10.00),
(5, 'Final Project', 'Project', 100.00),
(6, 'Quiz 3', 'Quiz', 10.00),
(7, 'Assignment 2', 'Assignment', 30.00),
(8, 'Final Exam', 'Exam', 100.00),
(9, 'Quiz 4', 'Quiz', 10.00),
(10, 'Lab Test', 'Lab', 40.00);

INSERT INTO Grades (enrollment_id, assessment_id, score) VALUES
(1, 1, 8.00),
(2, 2, 18.00),
(3, 3, 45.00),
(4, 4, 9.00),
(5, 5, 95.00),
(6, 6, 7.00),
(7, 7, 28.00),
(8, 8, 90.00),
(9, 9, 9.50),
(10, 10, 35.00);

INSERT INTO Course_Instructors (course_id, instructor_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);


select * from Courses;
select * from Students;
select * from Instructors;
select * from Enrollments;
select * from Assessments;
select * from Grades;
select * from Course_Instructors;