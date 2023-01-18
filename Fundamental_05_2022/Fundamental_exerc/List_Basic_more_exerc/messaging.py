numbers = input().split()
output_message = ''
index_list = []
message_list = [x for x in input()]

for i in range(len(numbers)):
    sum_index = 0
    for ch in numbers[i]:
        sum_index += int(ch)
    index_list.append(sum_index)

for j in range(0,len(index_list)):
    ll = len(message_list)
    index_list[j] = index_list[j] % ll
    output_message += message_list.pop(index_list[j])

print(output_message)

