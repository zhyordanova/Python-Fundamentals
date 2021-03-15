courses = {}

data = input()

while not data == "end":
    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

    data = input()

for courses, students in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{courses}: {len(students)}")
    for student in sorted(students):
        print(f"-- {student}")