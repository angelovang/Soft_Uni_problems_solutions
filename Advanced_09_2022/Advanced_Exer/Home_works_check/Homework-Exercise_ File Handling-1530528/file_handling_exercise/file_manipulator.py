import os
from os.path import exists
from os import remove
import re
while True:
    command = input().split("-")
    if command[0] == "End":
        break

    if command[0] == "Create":
        file_name = command[1]
        with open(f"text_files/file_manipulator/{file_name}", "w+") as text_file:
            if os.path.exists(f"text_files/file_manipulator/{file_name}"):
                text_file.write("")
    elif command[0] == "Add":
        file_name = command[1]
        contents = command[2]
        with open(f"text_files/file_manipulator/{file_name}", "a+") as text_file:
            text_file.writelines(contents + "\n")
    elif command[0] == "Replace":
        file_name = command[1]
        word_to_be_replaced = command[2]
        replacement = command[3]
        if os.path.exists(f"text_files/file_manipulator/{file_name}"):          #може и с try, except
            with open(f"text_files/file_manipulator/{file_name}", "r+") as file:
                text = file.readlines()
                for i in range(len(text)):
                    text[i] = text[i].replace(word_to_be_replaced, replacement)
                file.close()
                with open(f"text_files/file_manipulator/{file_name}", "w+") as file:
                    file.write(''.join(text))
        else:
            print("An error occurred")

    elif command[0] == "Delete":
        file_name = command[1]
        if os.path.exists(f"text_files/file_manipulator/{file_name}"):
            os.remove(f"text_files/file_manipulator/{file_name}")
        else:
            print("An error occurred")
