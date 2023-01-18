number_lines = int(input())
positive = []
negative = []
sum_of_negatives = 0
for lines in range(number_lines):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
        sum_of_negatives += number
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum_of_negatives}')
