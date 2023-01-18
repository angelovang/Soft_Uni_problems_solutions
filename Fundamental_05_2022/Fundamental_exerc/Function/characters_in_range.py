def char_in_range():
    a = input()
    b = input()
    char_list = []
    for i in range(ord(a)+1,ord(b)):
        char_list.append(chr(i))
    return char_list

print(*char_in_range())
