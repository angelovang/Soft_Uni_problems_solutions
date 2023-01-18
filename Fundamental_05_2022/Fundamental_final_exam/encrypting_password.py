import re

pattern = r'(.+)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})\<\1'

num_lines = int(input())

for i in range(num_lines):
    password = input()
    matches = re.findall(pattern,password)
#    print(matches)
    if matches :
        result = ''
        for i in range(1,len(matches[0])):
            result += matches[0][i]
        print(f"Password: {result}")
    else:
        print(f'Try another password!')


