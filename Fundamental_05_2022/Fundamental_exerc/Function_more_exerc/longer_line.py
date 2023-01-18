from math import floor,sqrt


def line_coordinates():
    line_coord = [[float(input()), float(input())] for i in range(2)]
    l_1 = line_coord[0][0] * line_coord[0][0] + line_coord[0][1] * line_coord[0][1]
    l_2 = line_coord[1][0] * line_coord[1][0] + line_coord[1][1] * line_coord[1][1]
    if l_1 <= l_2:
        return line_coord
    else:
        line_coord = line_coord[::-1]
        return line_coord


def line_len(coord):
    l = sqrt((coord[0][0] - coord[1][0]) * (coord[0][0] - coord[1][0]) + \
             (coord[0][1] - coord[1][1]) * (coord[0][1] - coord[1][1]))
    return l


def line_floor_and_print(line_par):
    for i in range(2):
        for j in range(2):
            line_par [i][j] = floor(line_par [i][j])
        line_par[i] = tuple(line_par[i])
        print(line_par[i],end='')
    return line_par


first_line = line_coordinates()
second_line = line_coordinates()

first_line_len = line_len(first_line)
second_line_len = line_len(second_line)

if first_line_len >= second_line_len:
    first_line = line_floor_and_print(first_line)
else:
    second_line = line_floor_and_print(second_line)




