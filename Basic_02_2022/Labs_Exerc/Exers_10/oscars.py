actor_name = input()
start_points = float(input())
jury_br = int(input())

total_point = start_points
for j in range(jury_br):
    jury_name = input()
    jury_point = float(input())
    actor_point = len(jury_name) * jury_point / 2
    total_point += actor_point
    if total_point > 1250.5 :
        break

if total_point > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_point:.1f}!')
else:
    diff = 1250.5 - total_point
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')


