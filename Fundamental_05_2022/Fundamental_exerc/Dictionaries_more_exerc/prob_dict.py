from collections import defaultdict
# Python3 code to demonstrate
# Sort nested dictionary by key
# using OrderedDict() + sorted()
from collections import OrderedDict
from operator import getitem

# initializing dictionary
test_dict = {'Nikhil': {'roll': 24, 'marks': 17},
             'Akshat': {'roll': 54, 'marks': 12},
             'Akash': {'roll': 12, 'marks': 15}}

# printing original dict
print("The original dictionary : " + str(test_dict))

# using OrderedDict() + sorted()
# Sort nested dictionary by key
res = sorted(test_dict.items(),key=lambda x: getitem(x[1], 'roll'))

# print result
print("The sorted dictionary by marks is : " + str(res))


s = [('yellow', 1), ('blue', 4), ('yellow', 3), ('blue', 2), ('red', 1)]
d = defaultdict(dict)
for k, v in s:
    d.setdefault(k,v)
print(d)
print(dict(sorted(d.items())))

# 1: Find sum of sharpness values using sum() function


# Python code to find sum values within nested dictionaries
weapons = {'': None, 'sword': {'steel': 151,
                               'sharpness': 100,
                               'age': 2, },

           'arrow': {'steel': 120,
                     'sharpness': 205,
                     'age': 1, }}

sumValue1 = sum(d['sharpness'] for d in weapons.values() if d)
sumValue2 = sum(d['steel'] for d in weapons.values() if d)

print(sumValue1)
print(sumValue2)

# 2 : Using Iteration to convert it into key:value pair.


# Python code to find sum values within nested dictionaries

weapons = { '' :{},'sword': {'steel': 151,
                               'sharpness': 100,
                               'age': 2, },

           'arrow': {'steel': 120,
                     'sharpness': 205,
                     'aage': 1, }}

sum = 0

# iterating key value pair
for key, value in weapons.items():
    a = value.keys()
    print(a)
    if value and 'sharpness' in value.keys():
        # Adding value of sharpness to sum
        sum += value['sharpness']

    # printing sum
print(sum)