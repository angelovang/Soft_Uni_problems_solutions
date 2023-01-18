number_of_lines = int(input())
total_sum = 0

for line in range(number_of_lines):
    current_char = input()
    total_sum += ord(current_char)

print(f'The sum equals: {total_sum}')
