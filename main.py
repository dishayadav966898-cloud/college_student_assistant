

#COLLEGE STUDENT ASSISTANT
print("1.study time calculator")
print("2.attendance calculator")
print("3.CGPA calculator")
print("4.college expense calculator")
print("5.exit")

choice = int(input("enter your choice:"))
print("your choice" , choice)

if choice == 1:
    def study_time():
        print("study time calculator selected")
        total_hours=int(input("enter the total available study hours:"))
        subjects=int(input("enter your number of subjects:"))
        time_per_subject = total_hours/subjects
        print("study time for each subject=",time_per_subject,"hours")
    
    study_time()
elif choice == 2:
    def attendance():
        print("attendance calculator selected")
        total_classes=int(input("enter total classes:"))
        attended_classes = int(input("enter attended classes:"))
        attendance_percent=(attended_classes / total_classes)*100
        print("your attendance=" , attendance_percent,"%")
    attendance()

elif choice == 3:
    print("CGPA calculator selected")
    subjects=int(input("enter the number of subjects:"))
    total=0
    for i in range(subjects):
        grade = int(input("enter grade point:"))
        total=total + grade
    cgpa = total/subjects
    print("your CGPA" , cgpa)
elif choice == 4:
    print(" college expense  calculator selected")
    monthly_expense=int(input("enter your monthly expense:"))
    months=int(input("enter number of months:"))
    total_expense=monthly_expense * months
    print("your total college expense=" , total_expense)
elif choice == 5:
    print("thanku for using college student assistant!")
else:
    print("invalide choice")


    