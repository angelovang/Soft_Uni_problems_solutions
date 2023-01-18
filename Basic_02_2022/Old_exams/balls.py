from math import ceil , floor
num = int(input())

total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
divides_black_balls = 0

for i in range(num):
    color = input()
    if color == 'red' :
        total_points += 5
        red_balls += 1
    elif color == 'orange' :
        total_points += 10
        orange_balls += 1
    elif color == 'yellow' :
        total_points += 15
        yellow_balls += 1
    elif color == 'white' :
        total_points += 20
        white_balls += 1
    elif color == 'black' :
        total_points= floor(total_points / 2)
        divides_black_balls += 1
    else:
        other_balls += 1


print(f'Total points: {total_points}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_balls}')
print (f'Divides from black balls: {divides_black_balls}')


