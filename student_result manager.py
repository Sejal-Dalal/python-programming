student = {}
while True:
    print("-------STUDENT RESULT MANAGER APP-------")
    print("1.  Add Student")
    print("2.  View Student")
    print("3.  Check result")
    print("4.  Exit")

    choice = input("Enter your choice:")
    if choice=="1":
        name = input("Enter your name:")
        marks = int(input("Enter your marks:"))
        student[name] = marks

    elif choice=="2":
        if not  student:
            print("student not found")
        else:
            for name, marks in student.items():
                print(name,":",marks)

    elif choice=="3":
        name = input("Enter student name:")
        if name in student:
            student[name]=marks
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("student not found")

    elif choice=="4":
        print("EXITING")
        break

    else:
        print(" INVALID INPUT ,Please enter a valid choice")

