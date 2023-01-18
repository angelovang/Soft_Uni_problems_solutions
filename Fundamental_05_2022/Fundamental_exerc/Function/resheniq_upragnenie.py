#1

def smallest_number(some_numbers):
    return min(some_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
all_numbers = [first_number, second_number, third_number]
min_number = smallest_number(all_numbers)
print(min_number)


#2

def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract(first, second, third):
    sum_of_first_and_second_integers = sum_numbers(first, second)
    result = subtract(sum_of_first_and_second_integers, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number,second_number,third_number))


#3

def get_characters(first_character, second_character):
    collected_characters = []
    for current_character in range(ord(first_character) + 1, ord(second_character)):
        collected_characters.append(chr(current_character))
    return collected_characters


first_character = input()
second_character = input()
result = get_characters(first_character, second_character)
print(' '.join(result))



#4


#5

# numbers_as_string = input().split()
# numbers_as_digits = []
# for current_number in numbers_as_string:
#     numbers_as_digits.append(int(current_number))
numbers_as_digits = [int(s) for s in input().split()]
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)


#5.1

def is_even(number):
    if int(number) % 2 == 0:
        return True
    return False


numbers=  input().split()
filtered_numbers = []
for current_number in numbers:
    if is_even(current_number):
        filtered_numbers.append(int(current_number))
print(filtered_numbers)





#9.1

def length_is_valid(some_string):
    if 6 <= len(some_string) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def symbols_are_valid(some_string):
    if some_string.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def have_at_least_two_digits(some_string):
    digits_counter = 0
    for character in some_string:
        if character.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


some_password = input()
validated = [length_is_valid(some_password), \
             symbols_are_valid(some_password), \
             have_at_least_two_digits(some_password)]
if all(validated):
    print("Password is valid")


#9.2

def validation(some_string):
    password_is_valid = True
    if len(some_string) < 6 or len(some_string) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not some_string.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False
    digits_counter = 0
    for character in some_string:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    return password_is_valid


some_password = input()
is_valid = validation(some_password)
if is_valid:  # is valid == True
    print("Password is valid")


#10

def is_perfect(number):
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    if number == sum:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(is_perfect(number))



#11




def check_progress(bar_current_value):
    if bar_current_value == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{bar_current_value}% [{'%'*(bar_current_value // 10)}{'.' * (10 - bar_current_value // 10)}]\nStill loading..."


bar_value = int(input())
print(check_progress(bar_value))




#12


def calculate_factorial(number):
    for factorial in range(1, number):
        number *= factorial
    return number


first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_factorial(first_number)
second_number_factorial = calculate_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")
