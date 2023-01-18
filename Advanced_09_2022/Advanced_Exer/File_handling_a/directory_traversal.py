# Working files are in directory "txt_files"

import os

dir_path = input()
extensions = {}

for file_name in os.listdir(dir_path):
    full_name = os.path.join(dir_path, file_name)

    if os.path.isfile(full_name):
        extension = full_name.split('.')[-1]

        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(file_name)

sorted_extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in sorted_extensions:
    print(f'.{extension}')

    for file in sorted(files):
        print(f'- - - {file}')
