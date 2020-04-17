userList = input('Введите любое количество слов через пробел\n')
a = userList.split(' ')
i = 0
for itm in a:
    i += 1
    if len(itm) > 10:
        print(f'{i}. {itm[0:10]}')
    else:
        print(f'{i}. {itm}')


