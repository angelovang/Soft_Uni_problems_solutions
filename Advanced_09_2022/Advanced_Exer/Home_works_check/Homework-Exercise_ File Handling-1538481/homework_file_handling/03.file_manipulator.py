import os


def create_file(file: str):
    file = open(f'{file}', 'w')
    return file.close()


def add_content(file, text):
    with open(f'{file}', 'a') as demo_file:
        demo_file.write(f'{text}\n')


def replace_string(file, old_str, new_str):
    lines = []
    try:
        with open(f'{file}', 'r+') as file_data:
            for line in file_data:
                line = line.replace(old_str, new_str)
                lines.append(line)
        with open(f'{file}', 'w') as output_file:
            for line in lines:
                output_file.write(line)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file):
    try:
        os.remove(file)
    except FileNotFoundError:
        print("An error occurred")


command = input().split('-')
while command[0] != "End":
    if command[0] == 'Create':
        file_name = command[1]
        create_file(file_name)
    elif command[0] == "Add":
        file_name, content = command[1], command[2]
        add_content(file_name, content)
    elif command[0] == "Replace":
        file_name, old_string, new_string = command[1], command[2], command[3]
        replace_string(file_name, old_string, new_string)
    elif command[0] == "Delete":
        file_name = command[1]
        delete_file(file_name)

    command = input().split('-')
