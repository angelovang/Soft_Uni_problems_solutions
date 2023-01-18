start_string = input()
end_string = ''
explosion = False
a = 0

for i in range(len(start_string)):
    if a == 0:
        explosion = False
    if start_string[i] == '>' :
        if not explosion :
            explosion = True
            a = int(start_string[i+1])
            end_string += start_string[i]
        else:
            if a > 0:
                if end_string[-1] == '>':
                    a += int(start_string[i+1])
                end_string += start_string[i]

    else:
        if not explosion:
            end_string += start_string[i]
        else:
            if a > 0:
                a -= 1

print(end_string)
