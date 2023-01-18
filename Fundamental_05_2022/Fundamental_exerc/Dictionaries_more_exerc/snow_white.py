dwarfs_info = {}
separator_1 = ' <:> '
separator_2 = ' <-> '


def get_info(line_, dw_info):
    dw_name , hat_color , dw_physics = line_.split(separator_1)
    dw_physics = int(dw_physics)
    if dw_name in dw_info :
        if hat_color in dw_info[dw_name]:
            if dw_physics > dw_info[dw_name][hat_color]:
                dw_info[dw_name][hat_color]= dw_physics
            return dw_info
        else:
            dw_info[dw_name][hat_color] = dw_physics
            return dw_info
    else:
        dw_info[dw_name]={}
        dw_info[dw_name][hat_color] = dw_physics
        return dw_info


def get_color_dict(dwarf_dict):
    result ={}
    for key,value in dwarf_dict.items():
        for key_nested,value_nested in value.items():
            if key_nested not in result:
                result[key_nested]= {}
            result[key_nested].update({key:value_nested})
    return result


def sort_dw_info(dw_info):
    for name_ , hat_ in dw_info.items():
        dw_info[name_]= dict(sorted(dw_info.items(), key = lambda x : x[1].items()[1] ))
    return dw_info


# Collect information
while True:
    line_info = input()
    if line_info == 'Once upon a time':
        break
    else:
        dwarfs_info = get_info(line_info,dwarfs_info)

print(dwarfs_info)

#sort dw by colors
dwarfs_color = get_color_dict(dwarfs_info)
print(dwarfs_color)
prob = dict(sorted(dwarfs_color.items()))
print(prob)

s_dwarfs_info = sort_dw_info(prob)
print(s_dwarfs_info)


#print result
for name,hat in s_dwarfs_info.items():
    for hat_ , physic in hat.items():
        print(f'({name}) {hat_} <-> {physic}')
 #         f'({s_dwarfs_info[name][hat]}')
