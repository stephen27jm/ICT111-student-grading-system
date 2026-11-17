
STUDENT GRADING SYSTEM

Institution: MULUMGUSHI UNIVERSITY
School: SCHOOL OF ENGNEERING AND TECHNOLOGY
Department:COMPUTER SCIENCE AND IT
Course: ICT111 – PRINCIPLES OF PROGRAMING (PYTHON AND GIT)
Lab: Lab 2 – Student Grading System
Name: mwansa stephen
student number: 202608842

1. PROJECT DESCRIPTION
The Student Grading System is a console-based Python application developed to record student information, calculate grades, and generate class statistics.
The system allows users to enter student numbers, names, and marks. It automatically assigns grades and decisions according to the grading scale provided in the laboratory instructions.
The application also displays all registered students and calculates the class average, highest mark, lowest mark, number of passes, and number of failures.

2. OBJECTIVE
The main objectives of this project are:
1. To store student records using lists and dictionaries.
2. To apply conditional statements ("if", "elif", and "else") when assigning grades.
3. To use "for" and "while" loops to process student records.
4. To validate user inputs and prevent invalid data.
5. To calculate class statistics.
6. To practise version control using Git and GitHub.

3. INPUT - PROCESS - OUTPUT
A. Input
The system accepts the following information:
- Student number
- Student name
- Student mark
The user also enters menu options to select the required operation.

B. Process
The system performs the following operations:
- Validates student numbers and names to ensure they are not blank.
- Checks that student marks are between 0 and 100.
- Rejects non-numeric marks.
- Assigns grades using conditional statements.
- Stores student information in dictionaries inside a list.
- Displays registered student records.
- Calculates class statistics using loops.

C. Output
The system produces the following outputs:
- Student registration confirmation.
- Student number, name, mark, grade, and decision.
- Total number of students.
- Class average.
- Highest and lowest marks.
- Number of students who passed and failed.
- Error messages for invalid inputs.

4. GRADING SCALE
The following grading scale was provided in the laboratory instructions:
Mark Range| Grade| Decision
80–100| A| Excellent
65-74| B| Very good
50–64| C| Good
45–49| D| Pass
0–44| F| Fail

5. DATA STRUCTURES USED
List 
A list named "students" is used to store multiple student records.
Example:

students = []

Dictionary

Each student is stored as a dictionary containing five keys:

- "student_number"
- "name"
- "mark"
- "grade"
- "decision"

Example:

student = {
    "student_number": "MU001",
    "name": "John",
    "mark": 85,
    "grade": "A",
    "decision": "Excellent"
}

Why a List of Dictionaries?

A list of dictionaries is suitable because it allows the program to store multiple students, with each dictionary containing the information belonging to one student.

It also makes it easier to access, update, display, and process student records.

6. PYTHON CONCEPT APPLIED

The following Python concepts were used in developing the application:

Concept| Application
Variables| Store student information and statistics
Lists| Store multiple student records
Dictionaries| Store individual student details
Input| Accept information from the user
If/elif/else| Assign grades and decisions
While loop| Repeat the menu and validate inputs
For loop| Process and display student records
Try/except| Handle non-numeric mark inputs
Functions| Not required in this implementation
Break| Exit loops when appropriate
Append| Add student records to the list
Len| Count the number of students
Round| Display the class average to two decimal places

7. SYSTEM MENU

The application provides the following menu:

STUDENT GRADING SYSTEM

1. Add student
2. Display all
3. Class summary
4. Exit

Choose 1-4:

Menu Functions

Option 1: Add Student

Allows the user to enter a student's number, name, and mark. The system validates the information and automatically assigns a grade and decision.

Option 2: Display All

Displays all registered students together with their numbers, names, marks, grades, and decisions.

If no students have been registered, the system displays an informative message.

Option 3: Class Summary

Calculates and displays the total number of students, class average, highest mark, lowest mark, passes, and failures.

Option 4: Exit

Terminates the application.

8. INPUT VALIDATION

The application includes input validation to improve reliability.

The following conditions are checked:

1. Blank student numbers are rejected.
2. Blank student names are rejected.
3. Marks below 0 are rejected.
4. Marks above 100 are rejected.
5. Non-numeric marks are rejected without crashing the program.
6. Invalid menu options display a warning and return the user to the menu.

9. CLASS STATISTICS

The application calculates the following statistics:

- Total Students: Number of registered students.
- Class Average: Sum of all student marks divided by the total number of students.
- Highest Mark: The highest mark recorded.
- Lowest Mark: The lowest mark recorded.
- Passes: Number of students with marks greater than or equal to 50.
- Fails: Number of students with marks below 50.

The program also checks whether the student list is empty before calculating statistics to prevent division-by-zero errors.

10. PROGRAM TESTING

The following tests are required to verify the correctness of the application.

Test| Input/Action| Expected Behaviour
T1| Enter marks 79 and 80| Assign B and A respectively
T2| Enter marks 49 and 50| Assign F and D respectively
T3| Enter -1, 101, and abc| Reject invalid marks and request valid input
T4| Display summary before registering students| Display an informative empty-class message
T5| Enter an invalid menu option| Display a warning and return to the menu

TEST RESULTS

The observed results should be recorded after executing each test.

Test| Observed Result
T1| To be recorded after testing
T2| To be recorded after testing
T3| To be recorded after testing
T4| To be recorded after testing
T5| To be recorded after testing

11. REFLECTION

QUESTOIN 1: Why does the order of if/elif conditions matter at grade boundaries?

The order of "if/elif" conditions matters because Python executes the first condition that evaluates to True. Correct ordering ensures that students receive the correct grades according to their marks.

QUESTION 2: What error could arise when calculating the average of an empty list?

A ZeroDivisionError can occur when calculating the average because the total number of students is zero. This can be prevented by checking whether the list is empty before performing the division.

QUESTION 3: How would you adapt the program to handle two courses per student?

I would modify the student dictionary to include separate marks and grades for each course. This would allow the system to record and calculate results for two different courses for every student.

12. CHALLENGES ENCOUNTERED

During the development of the application, some challenges were encountered, including:

- Correctly applying indentation in Python.
- Understanding how to use lists and dictionaries together.
- Handling invalid user inputs.
- Correctly defining and updating variables when calculating class statistics.
- Ensuring that the menu repeats until the user selects the exit option.

These challenges helped improve my understanding of Python programming and debugging.

13. CONCLUSION

The Student Grading System demonstrates the application of fundamental Python programming concepts, including variables, lists, dictionaries, conditional statements, loops, and input validation.

The project provides a practical solution for recording student marks, assigning grades, displaying student records, and generating class statistics.

It also provides practical experience in using Git and GitHub for version control and project management.



END OF PROJECT DOCUMENTATION
