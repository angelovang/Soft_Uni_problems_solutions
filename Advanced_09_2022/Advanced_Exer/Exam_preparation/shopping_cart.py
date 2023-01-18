def shopping_cart(*meals):
    cart = {'Soup': [], 'Pizza': [], 'Dessert': []}

    for meal in meals:
        if meal == 'Stop':
            break

        meal_name = meal[0]
        product = meal[1]

        if meal_name == 'Soup' and len(cart['Soup']) < 3:
            if product not in cart[meal_name]:
                cart[meal_name].append(product)

        elif meal_name == 'Pizza' and len(cart['Pizza']) < 4:
            if product not in cart[meal_name]:
                cart[meal_name].append(product)

        elif meal_name == 'Dessert' and len(cart['Dessert']) < 2:
            if product not in cart[meal_name]:
                cart[meal_name].append(product)

    for product in cart.values():
        if len(product) > 0:
            break
    else:
        return "No products in the cart!"

    sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for y in sorted_cart:
        result += f"{y[0]}:\n"
        for el in sorted(y[1]):
            result += f' - {el}\n'
    return result


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
#
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
#
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))

