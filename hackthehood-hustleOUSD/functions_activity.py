#step 1
menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

#step 2
def total_price(item1, item2):
    total_sum = menu[item1] + menu[item2]
    return total_sum

print(total_price('Pizza', 'Burger'))

#step 3

def price_difference(item1, item2):
    total_difference = abs(menu[item1] - menu[item2])
    return total_difference

print(price_difference('Cheese', 'Hot dog'))

#step 4 

def inflation(item, number):
    menu[item] = menu[item] * number
    return menu

print(inflation('Pizza', 2))

#step 5

def deflation(item, number):
    menu[item] = menu[item] / number
    return menu

print(deflation('Pizza', 2))

#step 6
# This function allows you to order 3 items, add a tax to the cost and rounds the taxed cost to get a final cost
def order(item1, item2, item3, tax):
    base_cost = menu[item1] + menu[item2] + menu[item3]
    print('base cost:')
    print(base_cost)
    taxed_cost = base_cost * tax
    print('taxed cost:')
    print(taxed_cost)
    final_cost = round(taxed_cost)
    print('final cost:')
    return final_cost

print(order('Pizza', 'Hot dog', 'Ice cream', 1.5))








