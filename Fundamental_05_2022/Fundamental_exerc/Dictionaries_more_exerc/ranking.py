start_info = {}
ranking_info = {}

info = input()
while info != "end of contests":
    contest, password = info.split(':')
    start_info[contest] = password
    info = input()

submission = input()
while submission != 'end of submissions':
    contest, password, username, points = submission.split('=>')
    if contest in start_info.keys() and password in start_info.values():
        if username in ranking_info:
            if contest in ranking_info[username]:
                point = ranking_info[username][contest]
                if int(points) > point:
                    ranking_info[username].update({contest: int(points)})
            else:
                ranking_info[username].update({contest: int(points)})
        else:
            ranking_info[username] = {contest: int(points)}

    submission = input()

best_candidate = ''
total_points = 0
for student in ranking_info:
    sum = 0
    for lang in ranking_info[student]:
        sum += ranking_info[student][lang]
    if sum > total_points:
        best_candidate = student
        total_points = sum

s_ranking_info = {}
for user in ranking_info:
    s_ranking_info[user] = sorted(zip(ranking_info[user].values(), ranking_info[user].keys()), reverse=True)

ordered_name = sorted(ranking_info.keys())

print(f'Best candidate is {best_candidate} with total {total_points} points.')
print(f'Ranking:')
for name in ordered_name:
    print(f'{name}')
    for i in range(len(s_ranking_info[name])):
        print(f'#  {s_ranking_info[name][i][1]} -> {s_ranking_info[name][i][0]}')
