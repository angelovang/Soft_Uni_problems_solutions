student_info = {}

def get_contests_dict(participants_dict):
    result ={}
    for key,value in participants_dict.items():
        for key_nested,value_nested in value.items():
            if key_nested not in result:
                result[key_nested]= {}
            result[key_nested].update({key:value_nested})
    return result


def print_contest_data(contest, all_contests_data):
    print(f'{contest}: {len(all_contests_data[contest])} participants')
    result = sorted(all_contests_data[contest].items(),key= lambda x: (-x[1] , x[0]))
    for i in range(len(result)):
        print(f'{i+1}. {result[i][0]} <::> {result[i][1]}')
    return

def grade_sum(name_,stud):
    total_sum = 0
    for grade_ in stud[name].values():
        total_sum += grade_
    return total_sum

while True:
    line_info = input()
    if line_info == 'no more time':
        break
    else:
        name , contest , points = line_info.split(' -> ')
        points = int(points)
        if name in student_info and contest in student_info[name]:
            if points > student_info[name][contest]:
                student_info[name][contest] = points
        else:
            if name not in student_info:
                student_info[name] = {}
            student_info[name][contest] = points


contests_dict = get_contests_dict(student_info)

for cont in contests_dict:
    print_contest_data(cont,contests_dict )
print(f'Individual standings:')
#print(contests_dict)
#print(student_info)

indivdual_stat = {}
for name in student_info:
    indivdual_stat.update({name : grade_sum(name,student_info)})
indivdual_stat = sorted(indivdual_stat.items(), key= lambda x : (-x[1], x[0]))
#print(indivdual_stat)
for i in range(len(indivdual_stat)):
    print(f'{i+1}. {indivdual_stat[i][0]} -> {indivdual_stat[i][1]}')
