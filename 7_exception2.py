"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
  try:  
    if(not type(price) is int or not type(discount) is int or not type(max_discount) is int):
      raise TypeError('Должны быть числами')
    else:
      price = abs(int(price))
      discount = abs(int(discount))
      max_discount = abs(float(max_discount))
    if max_discount >= 100:
      raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
      return price
    else:
      return price - (price * discount / 100)

  except  TypeError:
    print('Должны быть числа')

  except ValueError as big_discount:
    print('Большая скидка')

if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
    print(discounted(100, 200, 200))
