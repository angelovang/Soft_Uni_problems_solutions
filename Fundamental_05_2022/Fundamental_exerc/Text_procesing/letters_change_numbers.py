start_line = [x for x in (input().replace('\t','')).split(' ') if x != '' ]

current_result = []
first_ch = end_ch = dig_str = ''
dig_int = total_sum = 0
res_s = res_e = 0

for given_str in start_line:
    given_str.replace('\t','')
    dig_int = int(given_str[1:-1])
    if given_str[0].isupper():
        res_s = dig_int / (ord(given_str[0]) - ord('A') + 1)
    else:
        res_s = dig_int * (ord(given_str[0]) - ord('a') + 1)
    if given_str[-1].isupper():
        res_e = res_s - (ord(given_str[-1]) - ord('A') + 1)
    else:
        res_e = res_s + (ord(given_str[-1]) - ord('a') + 1)
    current_result.append(res_e)

total_sum = sum(current_result)
print(f'{total_sum:.2f}')
