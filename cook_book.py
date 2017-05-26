with open ('C:/netology\python2.1\menu.txt', encoding='utf-8') as f:
 new_list = f.read()
 info_list = list(new_list.split())
 cook_dict = {}

 cook_dict[info_list[0]] = [
                {'ingridient_name': info_list[2], 'quantity': int(info_list[3]), 'measure': info_list[4]},\
                {'ingridient_name': info_list[5], 'quantity': int(info_list[6]), 'measure': info_list[7]}
                ]

 cook_dict[info_list[8]] = [
                {'ingridient_name': info_list[10], 'quantity': int(info_list[11]), 'measure': info_list[12]},\
                {'ingridient_name': info_list[13], 'quantity': int(info_list[14]), 'measure': info_list[15]},\
                {'ingridient_name': info_list[16], 'quantity': int(info_list[17]), 'measure': info_list[18]}
                ]

 cook_dict[info_list[19]] = [
                {'ingridient_name': info_list[21], 'quantity': int(info_list[22]), 'measure': info_list[23]},\
                {'ingridient_name': info_list[24], 'quantity': int(info_list[25]), 'measure': info_list[26]},\
                {'ingridient_name': info_list[27], 'quantity': int(info_list[28]), 'measure': info_list[29]},\
                {'ingridient_name': info_list[30], 'quantity': int(info_list[31]), 'measure': info_list[32]}
                ]
cook_book = cook_dict              


def get_shop_list_by_dishes(dishes, person_count):
      shop_list = {}
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
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
      person_count = int(input('Введите количество человек: '))
      dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
      shop_list = get_shop_list_by_dishes(dishes, person_count)
      print_shop_list(shop_list)

create_shop_list()