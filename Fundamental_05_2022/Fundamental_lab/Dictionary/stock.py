products_as_list = [x for x in input().split() ]
product_as_dict = {products_as_list[i]:products_as_list[i+1] for i in range(0,len(products_as_list),2)}
prod_for_check = [y for y in input().split()]

for prod in prod_for_check:
    if prod in product_as_dict:
        print(f'We have {product_as_dict[prod]} of {prod} left')
    else:
        print(f"Sorry, we don't have {prod}")

