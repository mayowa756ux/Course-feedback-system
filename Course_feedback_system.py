feedback_list = []

def add_feedback():
    student = input("Enter student name: ")
    course = input("Enter course name: ")
    comment = input("Enter feedback: ")
    feedback_list.append({
        "student": student,
        "course": course,
        "comment": comment
    })
    print("Feedback submitted successfully")

def view_feedback():
    if not feedback_list:
        print("No feedback available")
    else:
        for f in feedback_list:
            print("Student:", f["student"])
            print("Course:", f["course"])
            print("Feedback:", f["comment"])
            print("------------------")

def main():
    while True:
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_feedback()
        elif choice == "2":
            view_feedback()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
