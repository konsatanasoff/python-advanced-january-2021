n_lines = int(input())

student_data = {}
for _ in range(n_lines):
    student, grade = input().split()
    grade = float(grade)

    if student not in student_data:
        student_data[student] = []
    student_data[student].append(grade)

for (student, grades) in student_data.items():
    avg = sum(grades) / len(grades)
    grades_str = ' '.join(map(lambda grade: f"{grade:.2f}", grades))
    print(f"{student} -> {grades_str} (avg: {avg:.2f})")