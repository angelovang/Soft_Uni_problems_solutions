from collections import defaultdict

number_of_rows = int(input())
student_grades = defaultdict(list)

for i in range(number_of_rows):
    name , grade = input() , float(input())
    student_grades[name].append(grade)

for student in student_grades:
    average_grade = sum(student_grades[student])/len(student_grades[student])
    if average_grade >= 4.50:
        print(f'{student} -> {average_grade:.2f}')

