# Working files are in directory "txt_files"

import os

while True:
    command = input().split('-')
    com = command[0]

    if com == "End":
        break

    file_name = 'txt_files/' + command[1]

    if com == 'Create':
        current_file = open(file_name, 'w')
        current_file.close()

    elif com == 'Add':
        content = command[2] + '\n'
        current_file = open(file_name, 'a')
        current_file.write(content)
        current_file.close()

    elif com == 'Replace':
        old_string = command[2]
        new_string = command[3]

        try:
            with open(file_name, 'r') as current_file:  # I am opening the file as read only
                txt = current_file.readlines()          # I read the data in a 'List'

                for i in range(len(txt)):               # I modify the data
                    txt[i] = txt[i].replace(old_string, new_string)

            with open(file_name, 'w') as current_file:  # I delete the old data in the file and write the new data!
                current_file.writelines(txt)

        except FileNotFoundError:
            print('An error occurred')

    elif com == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')

    else:
        break