def data_types(a,b):
    if a == 'int':
        return int(b)*2
    elif a == 'real':
        return f'{(float(b) * 1.5):.2f}'
    elif a == 'string':
        return '$' + b + '$'

command = input()
num = input()
print(data_types(command,num))

 