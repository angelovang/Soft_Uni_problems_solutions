numbers_dictionary = {}

while True:
    line = input()
    if line == 'Search':
        break
    number_as_string = line
    try:
        number = int(input())
        if number not in numbers_dictionary:
            numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable must be an integer")

while True:
    line = input()
    if line == 'Remove':
        break
    try:
        number_as_string = line
        print(numbers_dictionary[number_as_string])
    except KeyError:
        print("Number does not exist in dictionary" )

while True:
    line = input()
    if line == "End":
        break
    number_as_string = line
    try:
        del numbers_dictionary[number_as_string]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)