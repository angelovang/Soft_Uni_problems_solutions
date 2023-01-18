start_index = int(input())
end_index = int(input())

for index in range(start_index,end_index + 1):
    current_char = chr(index)
    print(current_char,end=' ')
