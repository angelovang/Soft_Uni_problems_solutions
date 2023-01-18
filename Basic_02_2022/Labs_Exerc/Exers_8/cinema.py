type_projection = input()
rows = int(input())
columns = int(input())
income = 0
cinema_capacity = rows * columns
if type_projection == 'Premiere':
    income = cinema_capacity * 12
elif type_projection == 'Normal':
    income = cinema_capacity * 7.50
else:
    income = cinema_capacity * 5

print(f'{income:.2f} leva')

