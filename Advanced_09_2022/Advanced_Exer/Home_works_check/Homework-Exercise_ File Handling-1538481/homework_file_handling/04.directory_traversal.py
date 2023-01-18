import os
directory = input()
resources = {}
result = ''
# for loop to go through chosen directory, taking file path, check which are files and
# store them in a dictionary. Extensions as a key and file names as a value.
for file in os.listdir(directory):
    print(file)
    file_path = os.path.join(directory, file)

    if os.path.isfile(file_path):
        file_name, extension = file.split('.')

        if extension not in resources:
            resources[extension] = []

        resources[extension].append(file)
# sort out the keys alphabetically and file names inside the value list of each key
resources = {key: sorted(value) for (key, value) in sorted(resources.items(), key=lambda x: x[0])}

# Open/Create a file in a chosen directory as per assignment and
# collecting all the data in a string variable 'result'
with open(f'{directory}/report.txt', 'w') as report_file:
    for extension, file_name in resources.items():
        result += f".{extension}" + '\n'
        result += f"- - - {', '.join(file_name)}\n"

# writing required info in a created report file
    report_file.write(result)
print(result)