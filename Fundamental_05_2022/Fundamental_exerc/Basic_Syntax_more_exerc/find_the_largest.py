number = input()
num_list = sorted(number,reverse=True)
num_res = ''
for char in num_list:
    num_res += char
print(num_res)
