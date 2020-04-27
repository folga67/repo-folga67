# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('text1.txt', 'w', encoding='UTF-8')
a = input('Введите текст \n')
while a:
    my_file.write(a + '\n')
    a = input('Введите текст \n')
    if not a:
        break
my_file.close()

my_file = open('text1.txt', 'r', encoding="UTF-8")
content = my_file.readlines()
print(content)
my_file.close()



