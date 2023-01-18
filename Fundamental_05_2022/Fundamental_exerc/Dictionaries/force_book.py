from collections import defaultdict

force_users = defaultdict(list)


def check_user(s, u, d):
    for s in force_users:
        if u in force_users[s]:
            if d == 2:
                force_users[s].pop(force_users[s].index(u))
            return True

    return False


def func_1(side, user):
    d = 1
    is_user = check_user(side, user, d)
    if is_user:
        return
    else:
#        if side not in force_users:
#           force_users[side] = []
        force_users[side].append(user)
        return


def func_2(side, user):
    d = 2
    is_user = check_user(side, user, d)
    if is_user:
        force_users[side].append(user)
        print(f'{user} joins the {side} side!')
        return
    else:
#        if side not in force_users:
#            force_users[side] = []
        force_users[side].append(user)
        print(f'{user} joins the {side} side!')
        return


while True:
    info = input()
    if info == 'Lumpawaroo':
        break
    else:
        if '|' in info:
            info = info.split(' | ')
            force_side, force_user = info[0], info[1]
            func_1(force_side, force_user)
        else:
            info = info.split(' -> ')
            force_side, force_user = info[1], info[0]
            func_2(force_side, force_user)

for side in force_users:
    if len(force_users[side]) != 0:
        print(f'Side: {side}, Members: {len(force_users[side])}')
        for user in force_users[side]:
            print(f'! {user}')
