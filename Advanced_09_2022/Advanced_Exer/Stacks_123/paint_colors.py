from collections import deque

start_string = deque(x for x in input().split())

main_colors = ('red', 'yellow', 'blue', 'orange', 'purple', 'green')
sec_colors = {'orange': ('red', 'yellow'), 'purple': ('red', 'blue'), 'green': ('yellow', 'blue')}

left_string = ''
right_string = ''
collected_colors = []

while start_string:
    substring = ''
    main = False

    if len(start_string) > 1:
        left_string = start_string.popleft()
        right_string = start_string.pop()

        if (left_string + right_string) in main_colors:
            substring = left_string + right_string
            main = True

        elif (right_string + left_string) in main_colors:
            substring = right_string + left_string
            main = True

    else:
        substring = start_string.pop()
        if substring in main_colors:
            main = True
    print(start_string)
    print(main)
    if main:
        collected_colors.append(substring)
    else:
        if start_string:
            left_string = left_string[:-1]
            right_string = right_string[:-1]
            if left_string:
                start_string.insert(len(start_string) // 2, left_string)
            if right_string:
                start_string.insert(len(start_string) // 2, right_string)
    print(start_string)
for color in collected_colors:
    if color in sec_colors and \
            not (sec_colors[color][0] in collected_colors and sec_colors[color][1] in collected_colors):
        collected_colors.remove(color)

print(collected_colors)
