import os
import re
directory = input()
directory_len = len(re.split(r"[\\/]", directory))
result = []
extensions = {}

for dir_files in os.walk(directory):

    if len(re.split(r"[\\/]", dir_files[0])) > directory_len + 1:
        continue
    for filename in dir_files[2]:
        file = os.path.join(directory, filename)
        if "." in file:
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)

extensions = sorted(extensions.items(), key= lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}\n")

    for file in sorted(files):
        result.append(f"- - - {file}\n")

with open("text_files/dictionary_traverals/report.txt", 'w') as file:
    file.write(''.join(result))
