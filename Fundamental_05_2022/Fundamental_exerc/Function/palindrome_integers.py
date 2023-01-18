dig_numbers = input().split(', ')

def test_for_palindrom(in_list):
    for num in in_list:
        if num == num[::-1]:
            print(True)
        else:
            print(False)

test_for_palindrom(dig_numbers)

