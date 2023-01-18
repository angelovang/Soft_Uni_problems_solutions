from math import ceil
number_of_peopple = int(input())
capacity = int(input())

#courses = ceil(number_of_peopple / capacity)
courses = number_of_peopple // capacity
if number_of_peopple % capacity != 0:
    courses += 1

print(courses)
