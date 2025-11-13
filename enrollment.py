enrollment = {
    "IT101": {'Alice', 'Bob', 'Charlie'},
    "CS102": {'Bob', 'Diana'},
    "IS201": {'Charlie', 'Eve'}
}

print("Current Enrollment:")
for course in enrollment:
    print(f"{course}: {enrollment[course]}")

print("\nAdding student 'Frank' to CS102...")
enrollment["CS102"].add('Frank')
print("Removing student 'Alice' from IT101...")
enrollment["IT101"].discard("Alice")

print("\nUpdated Enrollment:")
for course in enrollment:
    print(f"{course}: {enrollment[course]}")

count_courses = {}
for course, students in enrollment.items():
    for student in students:
        count_courses[student] = count_courses.get(student, 0) + 1

student_multiple = {student for student, count in count_courses.items() if count > 1}
print(f"\nStudent enrolled in multiple courses: {student_multiple}")


unique_student = {student for student in count_courses}
print(f"\nAll unique students: {unique_student}")