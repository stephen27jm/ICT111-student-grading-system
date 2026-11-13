students = []

while True:
    print("\nSTUDENT GRADING SYSTEM")
    print("1. Add student")
    print("2. Display all")
    print("3. Class summary")
    print("4. Exit")

    option = input("Choose 1-4: ")

    if option == "1":
        print("\nADD STUDENT")
        
        student_number = input("Enter student number: ")
        
        while student_number.strip() == "":
            print("Student number cannot be blank.")
            student_number = input("Enter student number: ")

        name = input("Enter student name: ")

        while name.strip() == "":
            print("Student name cannot be blank.")
            name = input("Enter student name: ")

        while True:
            try:
                mark = float(input("Enter student mark: "))

                if mark < 0 or mark > 100:
                    print("Mark must be between 0 and 100.")

                else:
                    break

            except ValueError:
                print("Invalid input. Enter a numeric mark.")

        if mark >= 75:
            grade = "A"
            decision = "Excellent"

        elif mark >= 65:
            grade = "B"
            decision = "Very good"

        elif mark >= 50:
            grade = "C"
            decision = "Good"

        elif mark >= 45:
            grade = "D"
            decision = "Pass"

        else:
            grade = "F"
            decision = "Fail"

        student = {
            "student_number": student_number,
            "name": name,
            "mark": mark,
            "grade": grade,
            "decision": decision
        }

        students.append(student)

        print("\nStudent added successfully!")
        print("Grade:", grade)
        print("Decision:", decision)
    elif option == "2":
        print("\nDISPLAY ALL STUDENTS")

        if len(students) == 0:
            print("No students have been registered yet.")

        else:
            for student in students:
                print("----------------------------")
                print("Student Number:", student["student_number"])
                print("Name:", student["name"])
                print("Mark:", student["mark"])
                print("Grade:", student["grade"])
                print("Decision:", student["decision"])
    elif option == "3":
        print("\nCLASS SUMMARY")

        if len(students) == 0:
            print("No students available to calculate statistics.")

        else:
            total_students = len(students)
            total_marks = 0
            highest = students[0]["mark"]
            lowest = students[0]["mark"]
            passes = 0
            fails = 0

            for student in students:
                mark = student["mark"]

                total_marks += mark

                if mark > highest:
                    highest = mark

                if mark < lowest:
                    lowest = mark

                if mark >= 50:
                    passes += 1
                else:
                    fails += 1

            average = total_marks / total_students

            print("Total students:", total_students)
            print("Class average:", round(average, 2))
            print("Highest mark:", highest)
            print("Lowest mark:", lowest)
            print("Number of passes:", passes)
            print("Number of fails:", fails)
    elif option == "4":
        print("Thank you for using the system!")
        break
    else:
        print("invalid option. please choose 1-4.")