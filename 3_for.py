"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

classes = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def count_sell_avg(sell_phones):
  phones_sum = 0
  for sum in sell_phones:
    phones_sum += sum
    return phones_sum/len(sell_phones)

all_avg = 0
for one_product in classes:
  product_avg = count_sell_avg(one_product['items_sold'])
  print(f'Средняя количество продаж каждого товара {one_product["product"]}: {product_avg}')
  all_avg += product_avg
print(f'Средние продажи всех товаров: {all_avg/len(classes)}')


def all_sum(phones):
  phones_sum = 0
  for sum in phones:
    phones_sum += sum
    return phones_sum*len(phones)

all_avg = 0
for one_product in classes:
  product_avg = all_sum(one_product['items_sold'])
  print(f'Общее количество продаж каждого товара {one_product["product"]}: {product_avg}')
  all_avg += product_avg
print(f'Общие продажи всех товаров: {all_avg}')






  



  



