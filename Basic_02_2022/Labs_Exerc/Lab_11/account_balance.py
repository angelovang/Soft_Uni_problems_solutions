contrb = input()
total_sum = 0

while contrb != 'NoMoreMoney':
    if float(contrb) < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {float(contrb):.2f}')
    total_sum += float(contrb)
    contrb = input()
print (f'Total: {total_sum:.2f}')


