#1

first_list = input().split(", ")
second_list = input().split(", ")
substrings = []
for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word and not first_word in substrings:
            substrings.append(first_word)
            break
print(substrings)


#2

version = [int(number) for number in input().split(".")]
version[-1] += 1
for current_index in range(len(version) - 1, -1, -1):
    if version[current_index] > 9:
        version[current_index] = 0
        if current_index - 1 >= 0:
            version[current_index - 1] += 1
print('.'.join(str(number) for number in version))



#3

words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print('\n'.join(filtered_words))

#print('\n'.join([word for word in input().split() if len(word) % 2 == 0]))

#4

def positive_numbers(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_numbers(numbers):
    return [number for number in numbers if int(number) < 0]


def even_numbers(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd_numbers(numbers):
    return [number for number in numbers if int(number) % 2 != 0]


numbers_as_string = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers_as_string))}")
print(f"Negative: {', '.join(negative_numbers(numbers_as_string))}")
print(f"Even: {', '.join(even_numbers(numbers_as_string))}")
print(f"Odd: {', '.join(odd_numbers(numbers_as_string))}")


#5

def check_chairs(numbers_of_rooms):
    total_free_chairs = 0
    needed_chairs = 0
    for number_of_room in range(1, numbers_of_rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
    return total_free_chairs, needed_chairs


numbers_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(numbers_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")


#8
messages = input().split()
final_message = []
for message in messages:
    number = ""
    current_message = ""
    for character in message:
        if character.isdigit():
            number += character
        else:
            break
    message = message.replace(number, '')
    number = int(number)
    current_message += chr(number)
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    current_message += message
    final_message.append(current_message)

print(" ".join(final_message))




