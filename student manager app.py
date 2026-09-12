student= {}

while True:
    print("-----Welcome to the student manager------")
    print("1.Add Student")
    print("2.View Student")
    print("3.Check result")
    print("4.Exit")


    choice = input("Enter your choice:")
    if choice=="1":
        name = input("Enter your name:")
        marks = int(input("Enter your marks:"))
        student[name] = marks
    elif choice=="2":
        if not student:
            print("No student found")
        else:
            for name,marks in student.items():
                print(name,":",marks)
    elif choice=="3":
        name=input("Enter your name:")
        if name in student:
            marks=student[name]
            if marks>=40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student not found")
    elif choice=="4":
        print("Exiting")
        break
    else:
        print("Invalid choice")




                