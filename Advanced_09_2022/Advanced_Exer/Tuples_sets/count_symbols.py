text = input()
my_dict = {}
for ch in text:
    if ch not in my_dict:
        my_dict[ch]= 1
    else:
        my_dict[ch] += 1
for key in sorted(my_dict):
    print(f'{key}: {my_dict[key]} time/s')

