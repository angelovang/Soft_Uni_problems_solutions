key = int(input())
numbers_of_line = int(input())
result_string = ''
for i in range(numbers_of_line):
    current_char = input()
    result_string += chr(ord(current_char) + key)

print(result_string)

