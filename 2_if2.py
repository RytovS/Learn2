"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def example(word1,word2):
  if type(word1 and word2)!= str:
    return'0' 
  elif word1 == word2:
    return'1'
  elif len(word1)>len(word2):
    return'2'
  elif word2 == 'learn':
   return'3'
  else: 
    return'4'
 
print(example('sc', 'cscs'))



  