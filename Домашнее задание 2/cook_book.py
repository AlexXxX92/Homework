with open('recipes.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip() #l
        ingredients_count = int(f.readline().strip())
        ingredients = []
        for i in range(ingredients_count):
            data = f.readline().strip().split(' | ')

            ingredient_name = data[0]
            quantity = data[1]
            measure = data[2]
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        f.readline()
        cook_book[dish_name] = ingredients

    print(cook_book)

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for dish in dishes:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
        return shop_list
    print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))


