number_of_snowballs = int(input())

snowball_weight = 0
snowball_time = 0
snowball_quality = 0
snowball_value = 0

for s_balls in range(number_of_snowballs):
    s_weight = int(input())
    s_time = int(input())
    s_quality = int(input())

    s_value = (s_weight/s_time)**s_quality

    if s_value > snowball_value:
        snowball_weight = s_weight
        snowball_time = s_time
        snowball_quality = s_quality
        snowball_value = s_value

print(f'{snowball_weight} : {snowball_time} = {snowball_value:.0f} ({snowball_quality})')



