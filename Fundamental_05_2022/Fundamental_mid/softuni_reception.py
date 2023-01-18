employee_efficiency = []
for i in range(3):
    employee_efficiency.append(int(input()))
students_count = int(input())

efficiency_per_day = sum(employee_efficiency)
hours_counter = 0

while students_count >= efficiency_per_day:
    hours_counter += 1
    if hours_counter % 4 != 0 :
        students_count -= efficiency_per_day

if students_count > 0 :
    hours_counter += 1
    if hours_counter % 4 == 0:
        hours_counter += 1
print(f'Time needed: {hours_counter}h.')

