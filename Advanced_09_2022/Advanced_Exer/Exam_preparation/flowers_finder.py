from collections import deque

vowels = deque(input().split())
consonants = input().split()

words = {"rose":"rose", "tulip":"tulip", "lotus":"lotus", "daffodil":"daffodil"}
found = False

while vowels and consonants:
    first_letter = vowels.popleft()
    second_letter = consonants.pop()

    for name in words:

        if first_letter in name:
            words[name] = words[name].replace(first_letter,'')
            if words[name] == '':
                print(f'Word found: {name}')
                found = True
                break

        if second_letter in name:
            words[name] = words[name].replace(second_letter,'')
            if words[name] == '':
                print(f'Word found: {name}')
                found = True
                break
    if found:
        break


if not found:
    print(f'Cannot find any word!')
if vowels :
    print(f'Vowels left: {" ".join(vowels)}')
if consonants :
    print(f'Consonants left: {" ".join(consonants)}')
