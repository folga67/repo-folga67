# Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

my_file = open('text5.txt', 'w')
a = (input('Введите через пробел набор чисел')).split()
my_file.writelines(a)

def func():
   return sum(map(int, a))

print(func())

my_file.close()


