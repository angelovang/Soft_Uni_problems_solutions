students_info = {}

while True:
    command = input()
    s_id = []
    if ":" not in command:
        stc = command
        break
    else:
        name , id , course = command.split(':')
        id = int(id)
        s_id.append(id)
        s_id.append(course)
        students_info[name] = s_id

stc = stc.replace("_"," ")
for name in students_info:
    if students_info[name][1] == stc:
        print(f'{name} - {students_info[name][0]}')

