def create_cook_book():
    cook_book = dict()
    with open('menu.txt', encoding='utf-8') as f:
        for line in f:
            dish = line.strip()
            ingridients = list()
            index = int(f.readline().strip())
            for i in range(index):
                ingridient_name = f.readline().strip().split('|')
                cook_ingredient = {'ingridient_name': ingridient_name[0], 'quantity': int(ingridient_name[1]), \
                                  'measure': ingridient_name[2]}
                ingridients.append(cook_ingredient)
            f.readline()
            cook_book.update({dish: ingridients})

    return cook_book

def get_shop_list_by_dishes(dishes, person_count,cook_book):
      shop_list = {}
      cook_book = create_cook_book()
      for dish in dishes:
        for ingridient in cook_book[dish]:
          new_shop_list_item = dict(ingridient)

          new_shop_list_item['quantity'] *= person_count
          if new_shop_list_item['ingridient_name'] not in shop_list:
            shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
          else:
            shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
      return shop_list

def print_shop_list(shop_list):
      for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], \
                                shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
      person_count = int(input('Введите количество человек: '))
      dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
      cook_book = create_cook_book()
      shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
      print_shop_list(shop_list)

create_shop_list()