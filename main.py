from pprint import pprint

recipes = 'recipes.txt'

def catalog_reader(recipes: str) -> dict:
    with open(recipes, 'r', encoding='utf-8') as file:
        cook_book = {}    # создаем словарь
        for line in file:  # берем первую строку из файла
            bludo = line.strip()
            food_name = []
            for item in range(int(file.readline())):
                list_ingredients = file.readline() # ингридиенты
                list_ingredients_split = list_ingredients.split('|') # разделенный список по знаку
                list_ingredients_k_v = {'ingredient_name':' ', 'quantity': '0', 'measure': ' '} # создаем список с ключами и добавлянием в них данные ключ - значение
                list_ingredients_k_v['ingredient_name'] = list_ingredients_split[0].strip()
                list_ingredients_k_v['quantity'] = list_ingredients_split[1].strip()
                list_ingredients_k_v['measure'] = list_ingredients_split[2].strip()
                # food_name.append(list_ingredients.strip())
                food_name.append(list_ingredients_k_v)
            cook_book[bludo] = food_name
            file.readline()
            # pprint(cook_book)
        return cook_book



def get_shop_list_by_dishes(dishes, person_count):
    customer_order = [] # заказ клиента
    full_menu = [] # все блюда меню
    customer_order.append(dishes)
    for order, list in glob_cook_book.items(): # разделяю на название блюда и список ингридиентов
        full_menu.append(order)
        for list_ingridient in list: # распаковываю непосредственно список ингридиентов блюда
            for unpacking in customer_order: # распаковка заказа
                for dish in unpacking: # разбивем на отдельные части
                    if dish in full_menu: # поиск заказа в меню
                        if dish == order:
                            list_ingridient['quantity'] = int(list_ingridient['quantity']) * person_count
                            components_list = {'measure': ' ', 'quantity': 0}
                            components_list['measure'] = list_ingridient['measure']
                            components_list['quantity'] = list_ingridient['quantity']
                            ready_list = {list_ingridient['ingredient_name']: ''}
                            ready_list[list_ingridient['ingredient_name']] = components_list
                            print(ready_list)

glob_cook_book = catalog_reader(recipes)
pprint(get_shop_list_by_dishes(['Шарлотка'], 2))