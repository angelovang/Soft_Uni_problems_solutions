tournament_days = int(input())

day_wins = 0
day_loses = 0
day_sum = 0
total_wins = 0
total_loses = 0
total_sum = 0
result = ''
sport = ''
while tournament_days != 0:
    sport = input()
    while sport != 'Finish':
        result = input()
        if result == 'win':
            day_wins +=1
            day_sum += 20
        else:
            day_loses +=1
        sport = input()
    if day_wins > day_loses:
        day_sum *= 1.1
    total_sum += day_sum
    total_wins += day_wins
    total_loses += day_loses
    day_sum = 0
    day_wins = 0
    day_loses = 0
    sport = ''
    result = ''
    tournament_days -= 1

if total_wins > total_loses:
    total_sum *= 1.2
    print(f'You won the tournament! Total raised money: {total_sum:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_sum:.2f}')


