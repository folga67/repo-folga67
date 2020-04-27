# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# my_file = open('text2.txt', 'w', encoding='UTF-8')
# a = input('Введите текст \n')
# while a:
#     my_file.write(a + '\n')
#     a = input('Введите текст \n')
#     if not a:
#         break
# my_file.close()

my_file = open('text2.txt', 'r', encoding ='UTF-8')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    print(f'Количество символов {i+1} строки {len(content[i])}')
my_file.close()
my_file = open('text2.txt', 'r', encoding ='UTF-8')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

