from modules import user_management, course_management, faq_management


def display_menu():
    print("==== Management System ====")
    print("1. Login")
    print("2. Register")
    print("3. Add Course")
    print("4. View Courses")
    print("5. Add FAQ")
    print("6. View FAQs")
    print("7. Exit")


def main():
    c = False
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            user_management.login()
            c = True
        elif choice == '2':
            user_management.register()
        elif choice == '3':
            if c == True:
                course_management.add_course()
            else:
                print("Login first")
                user_management.login()
        elif choice == '4':
            course_management.view_courses()
        elif choice == '5':
            if c == True:
                faq_management.add_faq()
            else:
                print("Login first")
                user_management.login()
        elif choice == '6':
            faq_management.view_faqs()
        elif choice == '7':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")


main()
