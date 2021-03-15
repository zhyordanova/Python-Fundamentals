n = int(input())

students = {}

for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

filtered_students = {}

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        filtered_students[student] = average_grade

for student, av_grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{student} -> {av_grade:.2f}")


