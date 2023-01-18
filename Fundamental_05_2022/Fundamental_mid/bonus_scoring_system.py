from math import ceil
number_of_students = int(input())
number_of_lectures = int(input())
add_bonus = int(input())
max_bonus = 0
max_attend = 0

for i in range(number_of_students):
    current_attend = int(input())
    current_bonus = current_attend/number_of_lectures * (5+add_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        max_attend = current_attend

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attend} lectures.")
