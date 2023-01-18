numbers_dictionary = {}

line = input()

while line != "Search":
    # Passing non-integer type to the variable number
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')

    line = input()  # Missed input at end of loop !

line = input()

while line != "Remove":
    # Searching for a non-existent number
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()  # Missed input at end of loop !

line = input()

while line != "End":
    # Removing a non-existent number
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()  # Missed input at end of loop !

print(numbers_dictionary)
 