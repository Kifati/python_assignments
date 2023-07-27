from modules import file_handling

COURSES_FILE = "data/courses.txt"

def add_course():
    print("==== Add Course ====")
    course_name = input("Enter the course name: ")

    courses_data = file_handling.read_data(COURSES_FILE)

    if courses_data:
        courses = courses_data.split("\n")
        for course in courses:
            if course_name.lower() == course.lower():
                print("Course already exists.")
                return

    new_course_data = f"{course_name}\n"
    file_handling.append_data(COURSES_FILE, new_course_data)
    print(f"Course '{course_name}' added successfully.")
def view_courses():
    print("==== View Courses ====")
    courses_data = file_handling.read_data(COURSES_FILE)

    if courses_data:
        courses = courses_data.split("\n")
        print("Available Courses:")
        for course in courses:
            print(course)
    else:
        print("No courses found.")