name = input()

year_grade = 0
torn = 0
klas = 1
grade = 0
while True :
    grade = float(input())
    if grade >= 4 :
        year_grade += grade
        average_grade = year_grade / klas
        klas += 1
        if klas > 12 :
            print(f'{name} graduated. Average grade: {average_grade:.2f}')
            break
    if grade < 4:
        torn += 1
        if torn == 2:
            print(f'{name} has been excluded at {klas} grade')
            break

