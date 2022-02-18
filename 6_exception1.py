"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  try:
    while True:
      user_say = str(input('Как дела?: ')).lower()
      if user_say == 'хорошо':
        break
    else:
      user_say = str(input ('Как дела?')).lower()   

  except KeyboardInterrupt:
    print(' ПОКА ')

if __name__ == "__main__":
      hello_user()


