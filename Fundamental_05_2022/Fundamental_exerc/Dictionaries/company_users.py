from collections import defaultdict

company_data = defaultdict(list)

while True:
    command = input()
    if command == 'End':
        break
    else:
        command = command.split(' -> ')
        company_name , emploee_id = command[0] , command[1]
        if emploee_id not in company_data[company_name]:
            company_data[company_name].append(emploee_id)

for comp in company_data:
    print(f'{comp}')
    for i in range(len(company_data[comp])):
        print(f'-- {company_data[comp][i]}')

