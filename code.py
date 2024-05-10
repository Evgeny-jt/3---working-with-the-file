def recipes(compound):
    recipe = []
    ingredient = {}
    for i in range(int(compound[1])):
        recipe.append({'ingredient_name': '', 'quantity': '', 'measure': ''})
    key = compound[0]
    del compound[0:2]
    i = 0
    for ingredients in compound:
        ingredient_name = (ingredients[0:ingredients.find(' | ')])
        quantity_measure = ingredients[ingredients.find(' | ') + 3:len(ingredients)]
        quantity = (quantity_measure[0:quantity_measure.find(' | ')])
        measure = (quantity_measure[quantity_measure.find(' | ') + 3:len(quantity_measure)])
        recipe[i]['ingredient_name'] = ingredient_name
        recipe[i]['quantity'] = quantity
        recipe[i]['measure'] = measure
        i += 1
    return [key, recipe]


with open('recipes.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    compound = []
    for line in f.readlines():
        if '\n' != line:
            compound.append(line.strip())
        else:
            # recipes(compound)
            dish = recipes(compound)
            cook_book[dish[0]] = dish[1]
            compound = []
    else:
        dish = recipes(compound)
        cook_book[dish[0]] = dish[1]
        compound = []

print(cook_book)
