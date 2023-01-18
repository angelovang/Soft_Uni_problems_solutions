# bakery
data = input().split(' ')

# for loop
# for i in range(0, len(data), 2):
#     products_dict[data[i]] = int(data[i + 1])

# dict comprehension
products_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}

print(products_dict)

# 2.Stock

inventory = input().split(' ')
inventory_products = {inventory[i]: int(inventory[i + 1]) for i in range(0, len(inventory), 2)}

products_to_search = input().split(' ')

for product in products_to_search:
    if product not in inventory_products:
        print(f'Sorry, we don\'t have {product}')
    else:
        print(f'We have {inventory_products[product]} of {product} left')

# 3.Statistics

products_inventory = {}

while True:
    command = input()
    if command == 'statistics':
        break

    command = command.split(': ')
    product = command[0]
    quantity = int(command[1])

    if product not in products_inventory:
        products_inventory[product] = quantity
    else:
        products_inventory[product] += quantity

print('Products in stock:')
product_representation = [f'- {item}: {str(products_inventory[item])}' for item in products_inventory]
print('\n'.join(product_representation))
print(f'Total Products: {len(products_inventory)}')
print(f'Total Quantity: {sum(products_inventory.values())}')


# 6.Odd Occurrences
from collections import defaultdict

words = input().split(' ')
counter_of_words = defaultdict(int)

for word in words:
    counter_of_words[word.lower()] += 1

print(' '.join([word for word, count in counter_of_words.items() if count % 2 != 0]))

# 7.Word Synonyms

from collections import defaultdict

synonyms = defaultdict(list)
number = int(input())

for _ in range(number):
    word, synonym = input(), input()
    synonyms[word].append(synonym)

data = [f"{word} - {', '.join(synonym)}" for word, synonym in synonyms.items()]
print('\n'.join(data))