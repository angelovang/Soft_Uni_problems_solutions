courses = {}

while True:
    inp_data = input()
    if inp_data == 'end':
        break
    else:
        current_data = inp_data.split(' : ')
        course_name, student_name = current_data[0] , current_data[1]
        if course_name not in courses:
            courses[course_name] = [student_name]
        else:
            courses[course_name].append(student_name)

for c_n in courses:
    print(f'{c_n}: {len(courses[c_n])}')
    for i in range(len(courses[c_n])):
        print(f'-- {courses[c_n][i]}')



