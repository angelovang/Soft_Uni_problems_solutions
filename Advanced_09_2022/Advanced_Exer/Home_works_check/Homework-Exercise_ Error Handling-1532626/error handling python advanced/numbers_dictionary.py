numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        if number_as_string not in numbers_dictionary:
            numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable must be an integer")


    line = input()

new_line = input()

while new_line != "Remove":
    searched = new_line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    new_line = input()

third_line = input()

while third_line != "End":
    searched = third_line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    third_line = input()


print(numbers_dictionary)
