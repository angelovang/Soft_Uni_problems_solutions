import re
bought_furniture = {}
total_price = 0
total_cost = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
#pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
while True:
    command_line = input()
    if command_line == 'Purchase':
        break
    else:
        matches = re.findall(pattern,command_line)
        if matches:
            name = matches[0][0]
            total_price = float(matches[0][1]) * int(matches[0][2])
            total_cost += total_price
            bought_furniture[name]=total_price


print(f'Bought furniture:')
for name in bought_furniture:
    print(name)
print(f'Total money spend: {total_cost:.2f}')

