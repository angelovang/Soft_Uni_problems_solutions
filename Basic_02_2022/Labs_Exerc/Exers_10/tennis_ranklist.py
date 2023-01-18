from math import floor
turs_count = int(input())
start_points = int(input())

final_points = 0
tt_point = 0
t_point = 0
w_turs = 0
for i in range (turs_count):
    result = input()
    if result == 'W':
        t_point = 2000
        w_turs += 1
    elif result == 'F':
        t_point = 1200
    elif result == 'SF':
        t_point = 720
    else:
        t_point = 0
    tt_point += t_point
final_points = start_points + tt_point
point_per_math = tt_point / turs_count
percent_wins = w_turs / turs_count * 100

print(f'Final points: {final_points}')
print(f'Average points: {floor(point_per_math)}')
print(f'{percent_wins:.2f}%')

