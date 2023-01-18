def naughty_or_nice_list(names , *com_1,**com_2):
    result = {
        "Nice" : [],
        "Naughty" : [],
        "Not found" : [],
        }
    com_1 = [x.split('-') for x in com_1]

    for x in com_1:
        current_list = []
        index = 0

        for i in range(len(names)):
            if int(x[0]) == names[i][0]:
                current_list.append(names[i][1])
                index = i

        if len(current_list) == 1:
            result[x[1]].extend(current_list)
            names.pop(index)

    for name , value in com_2.items():
        current_list = []
        index = 0

        for i in range(len(names)):
            if name == names[i][1]:
                current_list.append(names[i][1])
                index = i

        if len(current_list) == 1:
            result[value].extend(current_list)
            names.pop(index)

    result['Not found'].extend([n[1] for n in names])
    res = ''
    for key , value in result.items():
        if value:
            res += f'{key}: {", ".join(value)}\n'

    return res


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
