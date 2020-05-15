# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class Exception:
    def __init__(self, deviden, devider):
        self.deviden = deviden
        self.devider = devider

    def zerodev(self):
        while True:
            try:
                 self.deviden = int(input('Введите делимое'))
                 self.devider = int(input('Введите делитель'))
                 print(self.deviden / self.devider)
            except:
                 print(f'Вы ввели ноль или не число. Деление невозможно\n')
            user_answer = input('Попробуйте еще? Да/Нет')
            if user_answer =='Да':
                print(try_except.zerodev())
            print(f'Вы вышли')
        else:
            print('Вы вышли')

try_except = Exception(5, 5)
print(try_except.zerodev())