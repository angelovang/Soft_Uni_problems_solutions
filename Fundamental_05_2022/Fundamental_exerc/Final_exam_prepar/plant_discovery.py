n_lines = int(input())
plants = {}


def get_info(n, plants_):
    for i in range(n):
        info = input().split('<->')
        plant = info[0]
        rarity = int(info[1])
        rating = 0
        if plant not in plants_:
            plants_[plant] = {'rarity': rarity, 'rating': []}
        else:
            plants_[plant]['rarity'] = rarity
    #    print(plants_)
    return plants_


def sort_plants(plants__):
    while True:
        command = input().split(': ')
        if command[0] == 'Exhibition':
            break
        else:
            parameters = command[1].split(' - ')
            plant = parameters[0]

            if plant not in plants__:
                print('error')
                continue

            if command[0] == 'Rate':
                rating = int(parameters[1])
                plants__[plant]['rating'].append(rating)

            elif command[0] == 'Update':
                new_rarity = int(parameters[1])
                plants__[plant]['rarity'] = new_rarity

            elif command[0] == 'Reset':
                plants__[plant]['rating'] = []

    return plants__


def exhibition(plants___):
    print(f'Plants for the exhibition:')
    for plant in plants___:
        if len(plants___[plant]['rating']) > 0 and sum(plants___[plant]['rating']) > 0:
            average_rating = sum(plants___[plant]['rating']) / len(plants___[plant]['rating'])
        else:
            average_rating = 0
        rarity = plants___[plant]['rarity']
        print(f"- {plant}; Rarity: {rarity:}; Rating: {average_rating:.2f}")

    return


plants = get_info(n_lines, plants)
plants = sort_plants(plants)
exhibition(plants)
