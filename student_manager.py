def stud_manager():
    students = []
    while True:
        print("Menu")
        print("1. Add student\n"
              "2. view all students\n"
              "3. Search student\n"
              "4. Show highest score\n"
              "5. Show average score\n"
              "6. Delete a student\n"
              "7. Sort student by score\n"
              "8. exit")

        try:
            choose = int(input("Select number from menu: "))
        except ValueError:
            print("please enter number")
            continue

        match choose:
            case 1:
                student_name = input("student name: ")
                try:
                    student_score = float(input(f"{student_name}'s score: "))
                except ValueError:
                    print("please enter number")
                    continue
                student_info = (student_name, student_score)
                students.append(student_info)
            case 2:
                print("\n==Students==")
                if students:
                    for i in range(len(students)):
                        print(f"{i+1}. {students[i]}")
                else:
                    print("the list is empty")
            case 3:
                search = input("Enter a name:")
                found = False
                for i in range(len(students)):
                    if search == students[i][0]:
                        print(
                            f"{i+1}. Name: {students[i][0]}, Score: {students[i][1]}")
                        found = True
                if not found:
                    print("The student is not found")

            case 4:
                if students:
                    highest_score = students[0][1]
                    clever_student = students[0][0]

                    for i in range(len(students)):
                        if students[i][1] > highest_score:
                            highest_score = students[i][1]
                            clever_student = students[i][0]

                    print(
                        f"{clever_student} has the highest score: {highest_score}")
                else:
                    print("No students in the list")
            case 5:
                if students:
                    total = 0
                    for i in range(len(students)):
                        total += students[i][1]
                    avg = total/len(students)
                    print(f"Average score = {avg}")
                else:
                    print("No students available to calculate average")
            case 6:
                search = input("Enter a name:")
                found = False
                for i in range(len(students)):
                    if search == students[i][0]:
                        del students[i]
                        found = True
                        break
                if not found:
                    print("The student is not found")
            case 7:
                def myfunc(i):
                    return i[1]
                students.sort(key=myfunc, reverse=True)

                print("\n== Students Sorted by Score ==")
                for student in students:
                    print(student)
            case 8:
                print("exiting program...")
                break


stud_manager()
