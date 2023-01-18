def shopping_list(budget, **products_info):
    types_of_product = 5


    if budget < 100:
        return f"You do not have enough budget."

    else:
        result = ''
        for key , volume in products_info.items() :
            price = float(products_info[key][0])
            quantity = int(products_info[key][1])
            total_price = price * quantity

            if total_price <= budget :
                budget -= total_price
                result +=f"You bought {key} for {total_price:.2f} leva.\n"
                types_of_product -= 1
                if types_of_product == 0 or budget == 0 :
                    break
        return result







print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))