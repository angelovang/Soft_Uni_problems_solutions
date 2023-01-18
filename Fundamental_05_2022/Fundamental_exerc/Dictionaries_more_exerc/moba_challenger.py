players_info = {}
separator_1 = ' -> '
separator_2 = ' vs '


def get_info(line_,pl_info):
    player_ , pos_ , skill_ = line_.split(' -> ')
    skill_ = int(skill_)
    if player_ in pl_info :
        if pos_ in pl_info[player_]:
            if skill_ > pl_info[player_][pos_]:
                pl_info[player_][pos_]= skill_
            return pl_info
        else:
            pl_info[player_][pos_] = skill_
            return pl_info
    else:
        pl_info[player_]={}
        pl_info[player_][pos_] = skill_
        return pl_info


def duel(line_,pl_inf):
    pl_1 , pl_2 = line_.split(' vs ')
    if pl_1 in pl_inf and pl_2 in pl_inf:
        for pos in pl_inf[pl_1]:
            if pos in pl_inf[pl_2]:
                if pl_inf[pl_1][pos] == pl_inf[pl_2][pos]:
                    return pl_inf
                else:
                    if pl_inf[pl_1][pos] > pl_inf[pl_2][pos]:
                        pl_inf.pop(pl_2)
                    else:
                        pl_inf.pop(pl_1)
                return pl_inf
        return pl_inf
    else:
        return pl_inf

def sort_pl_info(pl_info):
    for name_ , pos_ in pl_info.items():
        pl_info[name_]= dict(sorted(pl_info[name_].items(), key = lambda x : (-x[1] , x[0])))
    return pl_info

def skill_sum(name_,pl_inf):
    total_sum = 0
    for skill_ in pl_inf[name_].values():
        total_sum += skill_
    return total_sum

# Collect information
while True:
    line_info = input()
    if line_info == 'Season end':
        break
    else:
        if separator_1 in line_info:
            players_info = get_info(line_info,players_info)
        else:
            players_info = duel(line_info,players_info)

#print(players_info)

#sort players_info by Skills
s_players_info = sort_pl_info(players_info)
#print(s_players_info)

#total_Skills
total_skills = {}
for name in s_players_info:
    total_skills.update({name : skill_sum(name,s_players_info)})
s_total_skills = dict(sorted(total_skills.items(), key = lambda x : (-x[1] , x[0])))
#print(s_total_skills)
#print result
for name in s_total_skills:
    print(f'{name}: {s_total_skills[name]} skill')
    for pos, skill in s_players_info[name].items():
        print(f'- {pos} <::> {skill}')
