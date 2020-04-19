x = input('Введите числа через пробел').split()

for i, itm in enumerate(x):
    x[i] = int(itm)

print(f'{sum(x)}\n Введите еще числа или 0 для выхода')

y = input().split()


def func(x, y):
    for i, itm in enumerate(y):
        y[i] = int(itm)
    while y[i] != 0:
        return sum(x) + sum(y[0:i+1])
    else:
        return sum(x) + sum(y[0:i])


print(f'Сумма итого - {func(x, y)}')







